"""Python script to convert flavor csv."""

#!/usr/bin/env python3

import csv
from datetime import date


def format_row(row):
    """Format each row"""
    out_row = []
    for item in row:
        if not item.strip():
            out_row.append("n/a")
        elif ", " in item:
            out_row.append(item.replace(', ', '--'))
        else:
            out_row.append(item)
    return out_row


def main():
    """Go."""
    today = date.today().strftime("%Y-%m-%d")

    row_list = []
    in_file = "reports/stash_report.csv"
    out_file = f"reports/out_report-{today}.csv"
    with open(in_file, newline="") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            print(", ".join(format_row(row)))
            row_list.append(", ".join(format_row(row)))

    with open(out_file, "w", newline="") as file:

        writer = csv.writer(file, delimiter=';')
        for row in row_list.copy():
            writer.writerow([row])


if __name__ == "__main__":
    main()
