#!/usr/bin/env python3
"""
    Define a Python script that provides some stats about Nginx logs stored
    in MongoDB.
"""
from pymongo import MongoClient


def stats():
    """ Prints Nginx logs stored in MongoDB. """
    client = MongoClient('mongodb://localhost:27017')

    db = client.logs
    collection = db.nginx

    t_logs = collection.count_documents({})
    print("{} logs".format(t_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check = collection.count_documents({"method": "GET",
                                               "path": "/status"})
    print("{} status check".format(status_check))


if __name__ == "__main__":
    stats()
