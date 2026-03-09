#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import List, Dict

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination data, resilient to deletions.
        """
        indexed_data = self.indexed_dataset()
        
        # Verify index is in a valid range
        assert index is None or (0 <= index < len(indexed_data) + 1000)
        
        if index is None:
            index = 0
            
        data = []
        curr_idx = index
        # Collect page_size items, skipping missing keys
        count = 0
        while count < page_size:
            if curr_idx in indexed_data:
                data.append(indexed_data[curr_idx])
                count += 1
            curr_idx += 1
            
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": curr_idx
        }
