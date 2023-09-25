from abc import ABC, abstractmethod
import time
import random

#Base class for search 
class Search(ABC):
    """Abstract base class for searching."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def perform_search(self):
        pass

#Sub Class for Linear Search.
class LinearSearch(Search):
    """Subclass for Linear Search."""

    def __init__(self, items, target):
        super().__init__(items)
        self.target = target

    # Doing Linear Search.
    def perform_search(self):
        start_time = time.time()
        for index, item in enumerate(self._items):
            if item == self.target:
                end_time = time.time()
                return index, start_time, end_time
        end_time = time.time()
        return -1, start_time, end_time

class BinarySearch(Search):
    """Subclass for Binary Search."""
    def __init__(self, items, target):
        super().__init__(items)
        self.target = target

    # Doing Binary Search.
    def perform_search(self):
        start_time = time.time()
        left, right = 0, len(self._items) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if self._items[mid] == self.target:
                end_time = time.time()
                return mid, start_time, end_time
            
            elif self._items[mid] < self.target:
                left = mid + 1
            
            else:
                right = mid - 1

        end_time = time.time()
        return -1, start_time, end_time
        
if __name__ == "__main__":
    # Specifying different array sizes.
    data_sizes = [50, 500, 1000, 5000, 10000, 50000, 100000, 500000]
    lin_search_times = []
    bin_search_times = []

    for size in data_sizes:
        #Creating a list of random integers for different sizes of array
        my_list = [random.randint(1, 1000) for i in range(size)]

        #Getting the target to be found in the list
        #Using Try Except block to validate the data type of the target.
        while True:
            try:
                target = int(input("Enter the item that you want to search in the array: "))
                break
            except:
                print("Please enter an integer as a target to be foundd in the list: ")

        # Instantiating Linear Search
        search_instance_ls = LinearSearch(my_list, target)

        # Performing the search and printing the result
        result, s_ls_time, e_ls_time = search_instance_ls.perform_search()
        print(f"For the data size {size}")
        if result != -1:
            print(f"Item found in the array at index {result} \n")
        else:
            print("Item is not present in the array \n")

        
        ls_time = e_ls_time - s_ls_time
        print(f"Time taken to complete the search for data size of {size} using Linear search is {ls_time:.15f}\n")
        lin_search_times.append(ls_time)

        # Instantiating Binary Search
        search_instance_bs = BinarySearch(sorted(my_list), target)

        # Performing the search and printing the result
        result, s_bs_time, e_bs_time = search_instance_bs.perform_search()
        print(f"For the data size {size}")
        if result != -1:
            print(f"Item found in the array at index {result} \n")
        else:
            print("Item is not present in the array \n")

        
        bs_time = e_bs_time - s_bs_time
        print(f"Time taken to complete the search for data size of {size} using Binary search is {bs_time:.15f}\n")
        bin_search_times.append(bs_time)