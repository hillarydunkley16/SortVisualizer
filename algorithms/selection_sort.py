import time
from colors import *

def selection_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        minIndex = i
    
        for j in range(i+1, size):
            if data[j] < data[minIndex]:
                minIndex = j
        
        data[i], data[minIndex] = data[minIndex], data[i]
        drawData(data, [YELLOW if x == j or x == j +
            1 else BLUE for x in range(len(data))])
        time.sleep(timeTick)

        drawData(data, [BLUE for x in range(len(data))])
