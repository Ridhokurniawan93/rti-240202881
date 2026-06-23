"""
generate_data.py
Generate dataset sintetis untuk DBMS Benchmarking menggunakan Faker.
Seed=42 untuk reproducibility.

Usage:
    python generate_data.py
    python generate_data.py --volumes 50000 100000
    python generate_data.py --seed 42
"""

import os
import csv
import random
import argparse
import hashlib
from datetime import datetime, date
from faker import Faker

# ============================================================
# KONFIGURASI
# ============================================================
DEFAULT_SEED = 42
DEFAULT_VOLUMES = [50000, 100000, 250000, 500000, 1000000]
OUTPUT_DIR = "data"

CATEGORIES = [
    "GAME", "EDUCATION", "BUSINESS", "MEDICAL", "SOCIAL",
    "PHOTOGRAPHY", "SPORTS", "TRAVEL", "MUSIC", "FINANCE",
    "SHOPPING", "FOOD", "WEATHER", "NEWS", "HEALTH",
    "ENTERTAINMENT", "COMMUNICATION", "TOOLS", "PRODUCTIVITY", "LIFESTYLE"
]

CURRENCIES = ["USD", "EUR", "IDR", "GBP", "JPY"]
CONTENT_RATINGS = ["Everyone", "Teen", "Mature", "18+", "Kids"]
INSTALL_RANGES = ["1+", "10+", "100+", "1K+", "10K+", "100K+", "1M+", "10M+"]
SIZE_OPTIONS = [f"{i}M" for i in range(1, 101)] + [f"{i}k" for i in range(100, 999)]
ANDROID_VERSIONS = [f"{i}.0 and up" for i in range(4, 15)]


def generate_record(fake, idx):
    """Generate 1 record data app playstore."""
    return {
        "app_name": fake.catch_phrase() + " " + fake.word().capitalize(),
        "app_id": f"com.{fake.domain_word()}.{fake.word()}.{idx}",
        "category": random.choice(CATEGORIES),
        "rating": round(random.uniform(1.0, 5.0), 1),
        "rating_count": random.randint(0, 500000),
        "installs": random.choice(INSTALL_RANGES),
        "free": random.choice([True, False]),
        "price": round(random.uniform(0.0, 99.99), 2),
        "currency": random.choice(CURRENCIES),
        "size": random.choice(SIZE_OPTIONS),
        "min_android": random.choice(ANDROID_VERSIONS),
        "developer_id": f"dev_{fake.user_name()}_{random.randint(1, 9999)}",
        "released": fake.date_between(start_date="-5y", end_date="today").isoformat(),
        "last_updated": fake.date_between(start_date="-1y", end_date="today").isoformat(),
        "content_rating": random.choice(CONTENT_RATINGS),
        "ad_supported": random.choice([True, False]),
        "in_app_purchases": random.choice([True, False]),
        "editors_choice": random.choice([True, False]),
        "scraped_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def compute_checksum(filepath):
    """Hitung SHA256 checksum file."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def generate_dataset(volume, seed, output_dir):
    """Generate dataset CSV dengan jumlah record tertentu."""
    fake = Faker()
    fake.seed_instance(seed)
    random.seed(seed)

    filepath = os.path.join(output_dir, f"app_playstore_{volume}.csv")

    print(f"  Generating {volume:,} records -> {filepath}")

    fieldnames = [
        "app_name", "app_id", "category", "rating", "rating_count",
        "installs", "free", "price", "currency", "size", "min_android",
        "developer_id", "released", "last_updated", "content_rating",
        "ad_supported", "in_app_purchases", "editors_choice", "scraped_time"
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(volume):
            writer.writerow(generate_record(fake, i))

    checksum = compute_checksum(filepath)
    print(f"  Checksum SHA256: {checksum}")

    return filepath, checksum


def main():
    parser = argparse.ArgumentParser(description="Generate dataset untuk DBMS benchmarking")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED, help="Random seed (default: 42)")
    parser.add_argument("--volumes", type=int, nargs="+", default=DEFAULT_VOLUMES,
                        help="Volume data yang di-generate (default: 50K 100K 250K 500K 1M)")
    parser.add_argument("--output", type=str, default=OUTPUT_DIR, help="Output directory")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    print(f"=" * 60)
    print(f"DBMS Benchmarking - Dataset Generator")
    print(f"Seed: {args.seed}")
    print(f"Volumes: {[f'{v:,}' for v in args.volumes]}")
    print(f"Output: {os.path.abspath(args.output)}")
    print(f"=" * 60)

    checksums = {}
    for volume in args.volumes:
        filepath, checksum = generate_dataset(volume, args.seed, args.output)
        checksums[volume] = checksum

    # Simpan checksum ke file
    checksum_file = os.path.join(args.output, "checksums.txt")
    with open(checksum_file, "w") as f:
        for volume, checksum in checksums.items():
            f.write(f"app_playstore_{volume}.csv: SHA256:{checksum}\n")

    print(f"\n{'=' * 60}")
    print(f"Semua dataset berhasil di-generate!")
    print(f"Checksum tersimpan di: {checksum_file}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
