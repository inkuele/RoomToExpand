#!/bin/sh


# Change to the Script directory to execute the Python script from there
cd "$(dirname "$0")"

# Find all .dir directories in the parent directory and pass each to the Python script
for filename in ../TD_Patch_Files/*.dir; do
    python3 concat_dir_files.py "$filename"
done
