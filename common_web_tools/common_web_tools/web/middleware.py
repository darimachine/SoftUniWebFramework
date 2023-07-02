import time


def simple_middleware(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        response = get_response(request, *args, **kwargs)
        end_time = time.time()
        print(f"Executed in {end_time-start_time} seconds")
        return response
    return middleware