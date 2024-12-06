import time

def speed_test(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"{fn.__name__} metodu calisiyor...")
        result = fn(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Gecen sure: {run_time}")
        return result
    return wrapper



@speed_test
def sum_gen():
    return sum((x for x in range(10000000)))

@speed_test
def sum_list():
    return sum([x for x in range(10000000)])

sum_gen()
sum_list()