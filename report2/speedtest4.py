# int値の剰余
import time

i2 = 1
i3 = 2
start_time = time.process_time()

for i in range(1000000):
    i1 = i2 % i3

end_time = time.process_time()

print(end_time - start_time)

# 0.137814484