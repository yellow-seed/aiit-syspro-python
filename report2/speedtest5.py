# listへの挿入
import time

i2 = 1
i3 = 2
lists = []
start_time = time.process_time()

for i in range(1000000):
    lists.append(1)

end_time = time.process_time()

print(end_time - start_time)

# 0.084651902