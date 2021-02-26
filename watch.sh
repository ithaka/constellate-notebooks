#!/bin/sh
set -e

# To use this install
# pip install watchdog[watchmedo]


watchmedo shell-command \
    --patterns="*.ipynb;*.md" \
    --recursive \
    --command='jupyter-book build "${watch_src_path}"' \
    .