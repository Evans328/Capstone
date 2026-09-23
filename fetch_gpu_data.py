"""
fetch_gpu_data.py

Pulls the RightNow/TechPowerUp GPU specs dataset (2,800+ GPUs, NVIDIA/AMD/Intel)
and flattens it into a clean CSV for use in SQL, Excel, or further Python analysis.

Requires: pip install requests pandas
"""

import requests
import pandas as pd
from datetime import datetime

# Source: mirrors TechPowerUp's GPU database (Apache 2.0 licensed)
DATA_URL = "https://raw.githubusercontent.com/RightNow-AI/RightNow-GPU-Database/main/data/all-gpus.json"

# Backup mirror on Hugging Face, in case the GitHub URL ever moves
BACKUP_URL = "https://huggingface.co/datasets/Jr23xd23/gpu-database/raw/main/data/all-gpus.json"


def fetch_gpu_data():
    """Download the raw GPU JSON data."""
    print("Downloading GPU dataset...")
    try:
        resp = requests.get(DATA_URL, timeout=30)
        resp.raise_for_status()
    except requests.RequestException:
        print("Primary source failed, trying backup mirror...")
        resp = requests.get(BACKUP_URL, timeout=30)
        resp.raise_for_status()

    data = resp.json()
    print(f"Downloaded {len(data)} GPU records.")
    return data


def clean_gpu_data(data):
    """Flatten JSON into a tidy DataFrame with useful derived columns."""
    df = pd.json_normalize(data)

    # Parse release date, extract year
    df["releaseDate"] = pd.to_datetime(df["releaseDate"], errors="coerce")
    df["releaseYear"] = df["releaseDate"].dt.year

    # Keep only real, modern, discrete consumer/workstation GPUs.
    # Drops ancient ISA-era cards, integrated graphics, and console GPUs
    # that would otherwise skew any price/performance analysis.
    modern = df[
        (df["releaseYear"] >= 2014)
        & (df["vendor"].isin(["nvidia", "amd", "intel"]))
        & (df["slot"] != "IGP")
    ].copy()

    # Add a rough compute-per-dollar-ready performance column (FP32 TFLOPS)
    # Note: 'fp32' in the source data is already in TFLOPS
    if "fp32" in modern.columns:
        modern.rename(columns={"fp32": "fp32_tflops"}, inplace=True)

    # Select and order the columns most useful for a price/performance analysis
    keep_cols = [
        "name", "vendor", "manufacturer", "gpuName", "architecture", "generation",
        "releaseDate", "releaseYear", "foundry", "processSize",
        "baseClock", "boostClock", "memoryClock",
        "memorySize", "memoryType", "memoryBus", "memoryBandwidth",
        "shaders", "tmus", "rops", "tensorCores", "rtCores",
        "tdp", "suggestedPSU", "busInterface",
        "fp16", "fp32_tflops", "fp64",
        "url",
    ]
    keep_cols = [c for c in keep_cols if c in modern.columns]
    modern = modern[keep_cols]

    # Sort newest first, drop exact duplicate rows
    modern = modern.sort_values("releaseDate", ascending=False).drop_duplicates()

    return df, modern


def main():
    raw_data = fetch_gpu_data()
    full_df, modern_df = clean_gpu_data(raw_data)

    # Save both the full historical dataset and the filtered "modern" one
    full_path = "gpu_specs_full.csv"
    modern_path = "gpu_specs_modern.csv"

    full_df.to_csv(full_path, index=False)
    modern_df.to_csv(modern_path, index=False)

    print(f"\nSaved {len(full_df)} total records to {full_path}")
    print(f"Saved {len(modern_df)} modern discrete GPU records to {modern_path}")
    print(f"\nModern dataset covers {modern_df['releaseYear'].min():.0f}–{modern_df['releaseYear'].max():.0f}")
    print(f"Vendors: {modern_df['vendor'].value_counts().to_dict()}")


if __name__ == "__main__":
    main()
