#!/usr/bin/python3
"""
Module to convert csv to json
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert csv to json
    """
    try:
        with open(
            filename,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as fichier_csv:
            lecteur = csv.DictReader(fichier_csv)
            donne = list(lecteur)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(donne, f, indent=4)

        return True

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return False
    except (OSError, csv.Error, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return False
