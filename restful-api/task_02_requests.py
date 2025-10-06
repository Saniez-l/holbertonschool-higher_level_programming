#!/usr/bin/python3
import requests
import json
import csv
"""
Module for consuming and processing data from an API using Python
"""

def fetch_and_print_posts():
    """
    Fetch and print post

    """
    x = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {x.status_code}")

    if x.status_code == 200:
        posts = x.json()
        for post in posts:
            print(post["title"])

    else:
        print(f"code d erreur {x.status_code}")


def fetch_and_save_posts():
    """
    Fetch and save post in csv
    """
    x = requests.get('https://jsonplaceholder.typicode.com/posts')
    if x.status_code == 200:
        posts = x.json()
        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as fichier_csv:
            writer = csv.DictWriter(fichier_csv, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)

    else:
        print(f"code d erreur {x.status_code}")
