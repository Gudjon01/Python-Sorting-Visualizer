import time

def insertion_sort(data,draw_rects,tick):
    for _ in range(len(data)-1):
        for i in range(1,len(data)):
            while data[i-1] > data[i] and i>0:
                data[i], data[i-1] = data[i-1], data[i]
                i = i-1
            draw_rects(data)
            time.sleep(1/tick)
        return data
