import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Option A: Read from a file list
with open("all_paths.txt") as f:
    list_of_files = [line.strip() for line in f if line.strip()]

# Option B: Auto-discover every .py/.md/.txt under your project tree
# base = Path(".")
# list_of_files = [str(p) for p in base.rglob("*") if p.suffix in {".py",".md",".txt"}]

for filepath_str in list_of_files:
    filepath = Path(filepath_str)
    filedir = filepath.parent
    filename = filepath.name

    # Ensure parent directory exists
    if filedir and not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    # Create file if missing or zero-length
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Touched empty file: {filepath}")
    else:
        logging.info(f"Skipped (already exists): {filepath}")
