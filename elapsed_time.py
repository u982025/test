import time
def start_timer():
    start_time = None
    def elapsed():
        nonlocal start_time
        now = time.time()
        if start_time is None:
            start_time = now
            return None
        return (now - start_time)
    return elapsed
