"""
Client for tdm-pilot.org.
This project is in a pilot stage and functionality may change.
"""

import logging
import glob
import gzip
import json
import os
import sys
import zipfile
from pathlib import Path
from urllib.request import urlretrieve

import progressbar
import requests


from IPython.core.display import display, HTML

version = 0.26

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


SERVICE_URL = 'https://backend.tdm-pilot.org/'
#SERVICE_URL = "http://localhost:5000/"

if os.environ.get("COLAB_GPU") is not None:
    home = "/content"
else:
    home = str(Path.home())

datasets_dir = os.path.join(home, 'data')
Path(datasets_dir).mkdir(parents=True, exist_ok=True)


def display_terms_of_use():
    msg = """Use and download of datasets is covered by the <a target="_blank" href="https://tdm-pilot.org/terms-and-conditions/">Terms & Conditions of Use</a>"""
    display(HTML(msg))


def display_description(description):
    display(HTML(f"<p>{description.get('search_description')}</p><p>{description['num_documents']} documents.</p>"))


class ProgressBar():
    """
    Simple progress bar to provide feedback in Notebook UI.

    Adapted/copied from: https://stackoverflow.com/a/53643011/758157
    """
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar = progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()


def get_description(dataset_id):
    """
    Downloads dataset metadata as JSON.
    """
    url = SERVICE_URL + f"nb/dataset/{dataset_id}/meta"
    rsp = requests.get(url, headers={"User-Agent": "labs-tdm-client"})
    return rsp.json()


def get_metadata(dataset_id, fname=None, force=False):
    """
    Downloads a CSV of document metadata for all
    documents in the dataset.
    """
    description = get_description(dataset_id)
    _ = display_description(description)
    metadata_url = description.get("metadata_url")
    if metadata_url is None:
        raise Exception(f"Dataset {dataset_id} not found.")
    if fname is None:
        output_file = f"{dataset_id}.csv"
    else:
        output_file = f"{fname}.csv"
    output_path = os.path.join(datasets_dir, output_file)
    if (force is False) and (os.path.exists(output_path)):
        logging.info(f"Metadata file {output_path} exists. Not re-downloading.")
    else:
        logging.info(f"Downloading {dataset_id} metadata to {output_path}")
        _ = urlretrieve(metadata_url, output_path, ProgressBar())
    display_terms_of_use()
    return output_path


def get_dataset(dataset_id, fname=None, force=False):
    """
    Downloads the gzip'ed JSONL file of all documents
    in the requested dataset.
    """
    description = get_description(dataset_id)
    _ = display_description(description)
    download_url = description.get("download_url")
    if download_url is None:
        raise Exception(f"Dataset {dataset_id} not found.")
    if fname is None:
        output_file = f"{dataset_id}.jsonl.gz"
    else:
        output_file = f"{fname}.jsonl.gz"
    output_path = os.path.join(datasets_dir, output_file)
    if (force is False) and (os.path.exists(output_path)):
        logging.info(f"Dataset file {output_file} exists. Not re-downloading.")
    else:
        logging.info(f"Downloading {dataset_id} to {output_file}")
        _ = urlretrieve(download_url, output_path, ProgressBar())
    display_terms_of_use()
    return output_path


def dataset_reader(file_path):
    """
    Helper to read in gzip files and yield Python dictionary
    documents.
    """
    with gzip.open(file_path, "rb") as input_file:
        for row in input_file:
            yield json.loads(row)


def download_gutenberg_sample():
    """
    Helper to download and unzip sample full text data.
    """
    tp = os.path.join(datasets_dir, "gutenberg-sample.zip")
    p = os.path.join(datasets_dir, "gutenberg-sample")
    url = "https://ithaka-labs-public.s3.amazonaws.com/tdm/gutenberg-sample.zip"
    _ = urlretrieve(url, tp, ProgressBar())
    with zipfile.ZipFile(tp) as zr:
        zr.extractall(datasets_dir)
    os.remove(tp)
    logging.info(f"Gutenberg sample files downloaded to: {p}")
    return p


def install():
    """
    Install this client as a module.
    """
    from setuptools import setup

    setup(
        name='tdm_client',
        version=version,
        py_modules=['tdm_client'],
        install_requires=["requests", "progressbar"]
    )


if __name__ == "__main__":
    install()

