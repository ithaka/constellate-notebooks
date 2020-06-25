"""
Client for tdm-pilot.org.
This project is in a pilot stage and functionality may change.
"""

import logging
import gzip
import json
from pathlib import Path
import os
from urllib.request import urlretrieve
import sys

import progressbar
import requests

version = 0.1

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


SERVICE_URL = 'https://www.jstor.org/api/tdm/v1/'
#SERVICE_URL = "http://localhost:5000/"

home = str(Path.home())
datasets_dir = os.path.join(home, 'datasets')
if os.path.exists(datasets_dir) is not True:
    os.mkdir(datasets_dir)


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
    print("***", url)
    rsp = requests.get(url)
    return rsp.json()


def get_metadata(dataset_id, fname=None):
    """
    Downloads a CSV of document mentadata for all
    documents in the dataset.
    """
    description = get_description(dataset_id)
    metadata_url = description.get("metadata_url")
    if metadata_url is None:
        raise Exception(f"Dataset {dataset_id} not found.")
    if fname is None:
        output_file = f"{dataset_id}.csv"
    else:
        output_file = "{fname}.csv"
    logging.info(f"Downloading {dataset_id} metadata to {output_file}")
    output_path = os.path.join(datasets_dir, output_file)
    _ = urlretrieve(metadata_url, output_path, ProgressBar())
    return output_path


def get_dataset(dataset_id, fname=None):
    """
    Downloads the gzip'ed JSONL file of all documents
    in the requested dataset.
    """
    description = get_description(dataset_id)
    download_url = description.get("download_url")
    if download_url is None:
        raise Exception(f"Dataset {dataset_id} not found.")
    if fname is None:
        output_file = f"{dataset_id}.jsonl.gz"
    else:
        output_file = f"{fname}.jsonl.gz"
    output_path = os.path.join(datasets_dir, output_file)
    logging.info(f"Downloading {dataset_id} to {output_file}")
    _ = urlretrieve(download_url, output_path, ProgressBar())
    return output_path


def dataset_reader(file_path):
    """
    Helper to read in gzip files and yield Python dictionary
    documents.
    """
    with gzip.open(file_path, "rb") as input_file:
        for row in input_file:
            yield json.loads(row)
