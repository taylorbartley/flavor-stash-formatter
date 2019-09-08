"""Python script to convert flavor csv."""

#!/usr/bin/env python3

import csv
from datetime import date
import argparse


def format_row(row):
    """Format each row"""
    out_row = []
    for item in row:
        if not item.strip():
            out_row.append("n/a")
        elif ", " in item:
            out_row.append(item.replace(", ", "--"))
        else:
            out_row.append(item)
    return out_row


def file_stuff(in_file, out_file):
    """Read/Write files."""
    row_list = []

    with open(in_file, newline="") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            print(", ".join(format_row(row)))
            row_list.append(", ".join(format_row(row)))

    with open(out_file, "w", newline="") as file:

        writer = csv.writer(file, delimiter=";")
        for row in row_list.copy():
            writer.writerow([row])

def parse_that_shit():
    """Parse that shit."""
    parser = argparse.ArgumentParser(description="Take filename.")
    parser.add_argument("filename", help="Filename of report.")
    return parser.parse_args()

def main():
    """Go."""
    today = date.today().strftime("%Y-%m-%d")

    args = parse_that_shit()

    in_file = f"C:\\Users\\TBart\\Downloads/{args.filename}.csv"
    out_file = f"reports/out_report-{today}.csv"

    file_stuff(in_file=in_file, out_file=out_file)

    print("File formatted happily.")


if __name__ == "__main__":
    main()
