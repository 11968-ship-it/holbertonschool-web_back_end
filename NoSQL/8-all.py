#!/usr/bin/env python3
""" 8-all """

def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: pymongo Collection object

    Returns:
        List of documents (dict). Returns [] if no documents.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
