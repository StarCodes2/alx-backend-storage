#!/usr/bin/env python3
"""
    Defines a Python function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """ Returns all students sorted by average score. """
    pipe = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(pipe))
