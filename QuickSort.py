
import time

def partition(data, start, end, drawData, speed):
    border = start
    pivot = data[end]
    drawData(data, getColorArray(len(data), start, end, border, border))
    time.sleep(speed)
    for j in range(start, end):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), start, end, border, j, True))
            time.sleep(speed)
            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, getColorArray(len(data), start, end, border, j))
        time.sleep(speed)


    drawData(data, getColorArray(len(data), start, end, border, end, True))
    time.sleep(speed)
    data[border], data[end] = data[end], data[border]
    return border


def quick_sort(data, start, end, drawData, speed):
    if start >= end:
        return
    partitionIdx = partition(data, start, end, drawData, speed)
    quick_sort(data, start, partitionIdx - 1, drawData, speed)
    quick_sort(data, partitionIdx + 1, end, drawData, speed)

def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')
        
        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'
    return colorArray

