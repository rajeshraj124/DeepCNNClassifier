import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s: %(message)s')

package_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filename)) or (not os.path.getsize(filename)==0):
        logging.info(f"Creating file: {filename}")
        with open(filepath, "w") as f:
            pass # Create an empty file
            logging.info(f"Creating an empty file: {filepath}")
    else:
        logging.info(f"File: {filename} already exists")
