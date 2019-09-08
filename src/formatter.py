"""Python script to convert flavor csv."""

#!/usr/bin/env python3

import csv


def main():
    """Go."""
    with open("stash_report copy.csv", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            for item in row.copy():
                if item == " ":
                    item.replace(' ', "taco")
                print(item)

            # print(", ".join(row.copy()))


if __name__ == "__main__":
    main()
