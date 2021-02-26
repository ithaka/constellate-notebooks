#!/bin/sh
set -e

pip install watchdog[watchmedo]
jupyter-book build --all .

watchmedo shell-command \
    --patterns="*.ipynb;*.md" \
    --recursive \
    --command='jupyter-book build "${watch_src_path}"' \
    .