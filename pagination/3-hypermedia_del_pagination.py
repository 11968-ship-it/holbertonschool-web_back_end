#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination info that is
        resilient to deletions.
        """
        # 1. Verify index is within valid range
        all_data = self.indexed_dataset()
        assert index is not None and 0 <= index < len(self.dataset())

        data = []
        current_index = index
        
        # 2. Collect data items
        # We loop until we have enough data to fill the page_size
        while len(data) < page_size and current_index < len(self.dataset()):
            item = all_data.get(current_index)
            if item:
                data.append(item)
            current_index += 1

        # 3. Construct the response
        return {
            'index': index,
            'next_index': current_index,
            'page_size': len(data),
            'data': data
        }
