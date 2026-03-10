#!/usr/bin/env python3
""" 9-insert_school """

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection.

    Args:
        mongo_collection: pymongo Collection object
        **kwargs: key-value pairs to insert as the document

    Returns:
        The _id of the inserted document
    """
    if mongo_collection is None:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
