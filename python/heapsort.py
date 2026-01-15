import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    print(f"h {h}")
    return [heapq.heappop(h) for _ in range(len(h))]
if __name__ == "__main__":
    print(heapsort([5,4,3,2,1]))
