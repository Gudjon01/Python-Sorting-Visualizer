import time


def bubble_sort(data,draw_rects,tick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_rects(data)
                time.sleep(1/tick)
    return data
