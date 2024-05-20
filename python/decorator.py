import time


def tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: '{func.__name__}': {elapsed_time:.6f} seconds")
        return result
    return wrapper


@tiempo_ejecucion
def example_function():
    time.sleep(2)
    print("Function completed.")


example_function()
