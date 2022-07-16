# hashの参照
import time

i2 = 1
i3 = 2
lists1 = list(range(1, 1000000 + 1))
lists2 = list(range(1, 1000000 + 1))
dicts = dict(zip(lists1, lists2))
start_time = time.process_time()

for i in lists1:
    i1 = dicts[i]

end_time = time.process_time()

print(end_time - start_time)

# 0.11441477399999997