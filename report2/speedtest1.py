# int値の代入
import time

i2 = 0
start_time = time.process_time()

for i in range(1000000):
    i1 = i2

end_time = time.process_time()

print(end_time - start_time)

# 0.08331697299999999