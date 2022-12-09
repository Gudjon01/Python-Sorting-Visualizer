import time


def seletion_sort(data, draw_rects, tick):
    for _ in range(len(data) - 1):
        for i in range(len(data) - 1):
            min_value = i

            for j in range(i + 1, len(data)):
                if data[j] < data[min_value]:
                    min_value = j
            if min_value != i:
                data[min_value], data[i] = data[i], data[min_value]
            draw_rects(data)
            time.sleep(1/tick)
        return data
