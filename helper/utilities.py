from time import perf_counter


def timeme(function):
    def timed(*args, **kwargs):
        start = perf_counter()
        function(*args, **kwargs)
        end = perf_counter()
        print(f"    Processing time taken by function {function.__name__} is = {end-start : .15f} seconds")
    return timed