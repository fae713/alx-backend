#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i]
                                      for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, object]:
        """
        A method with two integer arguments:

        Args:
            index (int): The start index of the page. Defaults to None.
            page_size (int): The number of items per page. Defaults to 10.

        Returns a dict containing:
            index: the current start index of the return page.
            next_index: the next index to query with.
            page_size: the current page size.
            data: the actual page of the dataset.
        """
        assert index is None or isinstance(index, int), "must be none or 0"
        assert isinstance(page_size, int), "Page size must be positive."

        if index is None:
            index = 0

        valid_index = next((i for i in
                            sorted(self.__indexed_dataset.keys())
                            if i >= index), None)

        if valid_index is None:
            return {"index": index, "data": [],
                    "page_size": page_size, "next_index": None}

        end_index = min(valid_index + page_size,
                        len(self.__indexed_dataset))
        data = [self.__indexed_dataset[i]
                for i in range(valid_index, end_index)]
        next_index = end_index \
            if end_index < len(self.__indexed_dataset) else None

        return {"index": valid_index, "data": data,
                "page_size": page_size, "next_index": next_index}
