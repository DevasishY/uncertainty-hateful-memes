# src/data/load_hateful_memes.py
import os
import pandas as pd

DATA_DIR = "/kaggle/input/hateful-memes-dataset/data"  # adjust to your real path
IMG_DIR = os.path.join(DATA_DIR, "img")

print(DATA_DIR, "exists:", os.path.exists(DATA_DIR))
print(IMG_DIR, "exists:", os.path.exists(IMG_DIR))

def load_hateful_memes(split: str = "train") -> pd.DataFrame:
    """
    Load one split (train/dev/test) and add an img_path column.
    """
    if split not in {"train", "dev", "test"}:
        raise ValueError("split must be 'train', 'dev', or 'test'")

    jsonl_path = os.path.join(DATA_DIR, f"{split}.jsonl")
    print("Reading:", jsonl_path, "exists:", os.path.exists(jsonl_path))

    # jsonl => one JSON per line
    df = pd.read_json(jsonl_path, lines=True)

    # if img column is just a filename like "00001.png"
    df["img_path"] = df["img"].apply(lambda name: os.path.join(DATA_DIR, name))
    return df
