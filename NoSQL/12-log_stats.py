#!/usr/bin/env python3
""" 12-log_stats.py: display stats from the nginx collection in logs DB """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    # Total number of documents
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # HTTP methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of GET /status requests
    status_check = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
