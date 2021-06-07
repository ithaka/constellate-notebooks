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
import time
from urllib.request import urlretrieve

import progressbar
import requests


from IPython.core.display import display, HTML

version = 0.3

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


SERVICE_URL = 'https://backend.tdm-pilot.org/'
#SERVICE_URL = "http://localhost:8000/"

if os.environ.get("COLAB_GPU") is not None:
    home = "/content"
else:
    home = str(Path.home())

datasets_dir = os.path.join(home, 'data')
Path(datasets_dir).mkdir(parents=True, exist_ok=True)


def display_terms_of_use():
    msg = """Constellate: use and download of datasets is covered by the <a target="_blank" href="https://tdm-pilot.org/terms-and-conditions/">Terms & Conditions of Use</a>"""
    display(HTML(msg))

display_terms_of_use()


def display_description(description):
    display(HTML(f"<p>{description.get('search_description')}</p><p>{description['num_documents']} documents.</p>"))


def display_file_not_found_error(dataset_id, download_type):
    display(HTML(f"<p class=\"ansi-red-fg\">Dataset: {dataset_id} {download_type} not found.</p>"))


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
    url = SERVICE_URL + f"nb/v2/dataset/{dataset_id}"
    rsp = requests.get(url, headers={"User-Agent": "labs-tdm-client"})
    return rsp.json()


def _get_download_type_details(description, download_type):
    info = None
    for download in description["downloads"]:
        if download["name"] == download_type:
            info = download
            break
    return info


def _download_file(dataset_id, download_type, file_name=None, force=False):
    description = get_description(dataset_id)
    _ = display_description(description)
    info = _get_download_type_details(description, download_type)

    if (info is None):
        display_file_not_found_error(dataset_id, download_type)
        raise Exception(f"Dataset {dataset_id} {download_type} not found.")

    output_path = os.path.join(datasets_dir, file_name or info["file_name"])
    if (force is False) and (os.path.exists(output_path)):
        logging.info(f"File {output_path} exists. Not re-downloading.")
        return output_path

    attempts = 0
    delay = 5
    max_attempts = 10
    while info["status"] == "in-progress":
        attempts += 1
        logging.info(f"{dataset_id} is in progress. Waiting {delay} seconds.")
        time.sleep(delay)
        description = get_description(dataset_id)
        info = _get_download_type_details(description, download_type)
        if attempts > max_attempts:
            raise Exception(f"Dataset download {download_type} not found after delaying {delay * attempts} seconds.")

    if info["status"] != "complete":
        raise Exception(f"Dataset {dataset_id}. Unexpected error. {download_type} not found. Status {info['status']}")

    logging.info(f"Downloading {dataset_id} metadata to {output_path}")
    _ = urlretrieve(info["url"], output_path, ProgressBar())
    return output_path


def get_metadata(dataset_id, fname=None, force=False):
    """
    Downloads a CSV of document metadata for all
    documents in the dataset.
    """
    return _download_file(dataset_id, "sampled-metadata", file_name=fname, force=force)


def get_dataset(dataset_id, fname=None, force=False):
    """
    Downloads the gzip'ed JSONL file of all documents
    in the requested dataset.
    """
    return _download_file(dataset_id, "sampled-jsonl", file_name=fname, force=force)


def download(dataset_id, download_type, fname=None, force=False):
    return _download_file(dataset_id, download_type, file_name=fname, force=force)


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

