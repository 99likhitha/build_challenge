import threading
import time


class BlockingBuffer:
    """
    Custom FIFO blocking buffer using wait/notify.
    Satisfies:
    - Blocking queue behavior
    - Thread synchronization
    - Wait/notify mechanism
    """
    def __init__(self, max_size=5):
        self.buffer = []
        self.max_size = max_size
        self.condition = threading.Condition()

    def put(self, item):
        with self.condition:
            while len(self.buffer) >= self.max_size:
                self.condition.wait()
            self.buffer.append(item)
            self.condition.notify_all()

    def get(self):
        with self.condition:
            while len(self.buffer) == 0:
                self.condition.wait()
            item = self.buffer.pop(0)
            self.condition.notify_all()
            return item


class Producer(threading.Thread):
    """
    Producer that pushes items into the buffer.
    Does NOT send sentinel.
    """
    def __init__(self, source_data, buffer, delay=0.01):
        super().__init__()
        self.source_data = source_data
        self.buffer = buffer
        self.delay = delay

    def run(self):
        for item in self.source_data:
            time.sleep(self.delay)
            self.buffer.put(item)


class Consumer(threading.Thread):
    """
    Consumer that stops when it receives a sentinel (None).
    """
    def __init__(self, buffer, destination):
        super().__init__()
        self.buffer = buffer
        self.destination = destination

    def run(self):
        while True:
            item = self.buffer.get()
            if item is None:
                break
            self.destination.append(item)


def send_sentinels(buffer, num_consumers):
    for _ in range(num_consumers):
        buffer.put(None)
