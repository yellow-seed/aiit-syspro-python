# listの参照
import time

i2 = 1
i3 = 2
lists = [1] * 1000000
start_time = time.process_time()

for i in range(1000000):
    lists.pop()

end_time = time.process_time()

print(end_time - start_time)

# 0.086709615