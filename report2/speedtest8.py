# listのソート
import time
import random

i2 = 1
i3 = 2
lists = [random.randint(0, 1000000) for i in range(1000000)]
start_time = time.process_time()

lists.sort()

end_time = time.process_time()

print(end_time - start_time)

# 0.22300449200000005