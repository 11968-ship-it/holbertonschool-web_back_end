#!/usr/bin/env python3
""" 10-update_topics """

def update_topics(mongo_collection, name, topics):
    """
    Updates all documents in a MongoDB collection matching the school name,
    setting the 'topics' field to the provided list of topics.

    Args:
        mongo_collection: pymongo Collection object
        name (str): name of the school to update
        topics (list): list of topics to assign to the school
    """
    if mongo_collection is None or not name or not isinstance(topics, list):
        return
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
