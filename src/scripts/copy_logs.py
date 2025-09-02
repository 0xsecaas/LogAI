
import os
import shutil
from pathlib import Path
import sys

def copy_logs(sources):
    target_dir = "./data/"
    os.makedirs(target_dir, exist_ok=True)
    for path in sources:
        p = Path(path)
        if p.exists() and p.is_file():
            shutil.copy2(p, target_dir)
            print(f"Copied {p} -> {target_dir}")
        elif p.exists() and p.is_dir():
            for file in p.glob("*.log"):
                shutil.copy2(file, target_dir)
                print(f"Copied {file} -> {target_dir}")

if __name__ == "__main__":

    # Default system log paths (Linux)
    LOG_SOURCES = [
        "/var/log/syslog",
        "/var/log/messages",
        "/var/log/auth.log",
        "/var/log/kern.log",
        "/var/log/dmesg",
        "/var/log"  # copies *.log
    ]

    copy_logs(LOG_SOURCES)
