#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    Args:
        boxes (list): A list of boxes where each box is represented as a list
            of keys (indices) to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''

    # Get the total number of boxes
    n = len(boxes)

    # Set to keep track of the seen boxes
    seen_boxes = set([0])

    # Set to keep track of the unseen boxes
    unseen_boxes = set(boxes[0]).difference(set([0]))

    # Iterate until all boxes have been seen
    while len(unseen_boxes) > 0:
        # Get a box from the unseen boxes set
        boxIdx = unseen_boxes.pop()

        # Skip invalid box indices
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue

        # If the box has not been seen, add its keys to the unseen set
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)

    # Check if all boxes have been seen
    return n == len(seen_boxes)
