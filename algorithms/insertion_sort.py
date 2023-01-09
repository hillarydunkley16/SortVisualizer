import time
from colors import *


def insertion_sort(data, drawData, timeTick):
    # Traverse through 1 to len(arr)
    size = len(data)
    for i in range(1, size-1):
        value = data[i]
        j = i-1
        while j >= 0 and value < data[j]:
            data[j + 1] = data[j]
            j -= 1
            data[j + 1] = value
            drawData(data, [YELLOW if x == j or x == j +
                     1 else BLUE for x in range(len(data))])
            time.sleep(timeTick)

            drawData(data, [BLUE for x in range(len(data))])
