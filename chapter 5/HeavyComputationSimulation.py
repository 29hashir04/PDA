import time
import concurrent.futures
def count(number):
    for _ in range(100_000_000):
        pass
    return number * 100_000_000

def evaluate(item):
    result =  count (item)
    print(f"Item {item}, result {result }")

number_list = [1,2,3,4,5]

start_time = time.time()
for item in number_list:
    evaluate(item)
print(f"sequantial Execution: {time.time() - start_time:.2f}seconds")

start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for item in number_list:
        executor.submit(evaluate,item)
print(f"thread Pool Execution: {time.time() - start_time:.2f} seconds")

start_time = time.time()
with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    for item in number_list:
        executor.submit(evaluate, item)
    print(f"Process Pool Execution: {time.time() - start_time:.2f}seconds")


