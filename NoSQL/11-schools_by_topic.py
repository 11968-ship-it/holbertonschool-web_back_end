#!/usr/bin/env python3
""" 11-schools_by_topic """

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of documents where the 'topics' array contains the specified topic.

    Args:
        mongo_collection: pymongo Collection object
        topic (str): topic to search for

    Returns:
        List of documents (dict) matching the topic
    """
    if mongo_collection is None or not topic:
        return []
    return list(mongo_collection.find({"topics": topic}))
