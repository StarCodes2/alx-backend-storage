#!/usr/bin/env python3
"""
    Define a Python script that improves on 12-log_stats.py by adding the top
    10 of the most present IPs in the collection nginx of the database logs.
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

    pipe = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        { 
            "$sort": { "count": -1 }    # Sort by count in descending order
        },
        {
            "$limit": 10                # Limit the result to top 10
        }
    ]

    print("IPs:")
    for ip in collection.aggregate(pipe):
        print("{}: {}".format(ip['_id'], ip['count']))


if __name__ == "__main__":
    stats()
