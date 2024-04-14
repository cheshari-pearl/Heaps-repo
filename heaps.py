
import heapq

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3,1 ]
heapq.heapify(data)

print(data)


print(heapq.heappop(data))
print(data)

heapq.heappush(data, 9)
heapq.heappush(data,0)
print(data)







