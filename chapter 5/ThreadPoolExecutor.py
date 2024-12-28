from concurrent.futures import ThreadPoolExecutor
def cube(number):
    return number**3

numbers = [2,4,6,8]

executor = ThreadPoolExecutor(max_workers=2)

future = executor.submit(cube,3)

print('Single Task Result:', future.result())

results = executor.map(cube, numbers)
print("Mapped Results:", list (results))

executor.shutdown()

print("Executor Shut downed")

