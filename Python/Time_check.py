import time

start = time.time()
# Code block to test
sum([i for i in range(10)])
end = time.time()

print("Execution time:", end - start, "seconds")