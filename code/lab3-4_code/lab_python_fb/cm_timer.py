import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        cool_time = self.end_time - self.start_time
        print(f"time: {cool_time}")

@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    end_time = time.time()
    cool_time = end_time - start_time
    print(f"time: {cool_time}")


# with cm_timer_1():
#     time.sleep(5.5)

# with cm_timer_2():
#     time.sleep(5.5)