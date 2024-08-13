#!/usr/bin/env python3
"""
    Defines a Python function that returns the list of school having a
    specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic. """
    result = mongo_collection.find({"topics": topic})
    return [doc for doc in result]
