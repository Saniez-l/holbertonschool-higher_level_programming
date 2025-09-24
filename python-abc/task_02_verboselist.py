#!/usr/bin/python3
"""
This module Extending the Python List with Notifications
"""


class VerboseList(list):
    """
    Class extending the python list
    """
    def append(self, item):
        """
        Print a message with item
        """
        print(f"Added {item} to the list.")
        super().append(item)

    def extend(self, x):
        """
        Print a message with number of item added
        """
        count = len(x)
        print(f"Extended the list with {count} items.")
        super().extend(x)

    def remove(self, item):
        """
        Print a message with item
        """
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Print message with item
        """
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
