from assignment1.producer_consumer import (
    BlockingBuffer, Producer, Consumer, send_sentinels
)
import time


# 1. Basic flow
def test_basic_flow():
    buffer = BlockingBuffer(max_size=3)
    dest = []

    c = Consumer(buffer, dest)
    c.start()

    p = Producer([1,2,3], buffer)
    p.start()
    p.join()

    send_sentinels(buffer, 1)
    c.join()

    assert dest == [1,2,3]


# 2. Blocking queue behavior
def test_blocking_behavior():
    buffer = BlockingBuffer(max_size=1)
    dest = []

    c = Consumer(buffer, dest)
    c.start()

    p = Producer([1,2], buffer, delay=0.01)
    p.start()
    p.join()

    send_sentinels(buffer, 1)
    c.join()

    assert dest == [1,2]


# 3. Multiple producers
def test_multiple_producers():
    buffer = BlockingBuffer(max_size=3)
    dest = []

    c = Consumer(buffer, dest)
    c.start()

    p1 = Producer([1, 2], buffer)
    p2 = Producer([3, 4], buffer)

    p1.start(); p2.start()
    p1.join(); p2.join()

    send_sentinels(buffer, 1)
    c.join()

    assert sorted(dest) == [1, 2, 3, 4]


# 4. Multiple consumers
def test_multiple_consumers():
    buffer = BlockingBuffer(max_size=5)
    source = list(range(10))
    dest1, dest2 = [], []

    c1 = Consumer(buffer, dest1)
    c2 = Consumer(buffer, dest2)
    c1.start(); c2.start()

    p = Producer(source, buffer)
    p.start()
    p.join()

    send_sentinels(buffer, 2)

    c1.join()
    c2.join()

    combined = dest1 + dest2
    assert sorted(combined) == sorted(source)


# 5. Empty input
def test_empty_input():
    buffer = BlockingBuffer()
    dest = []

    c = Consumer(buffer, dest)
    c.start()

    p = Producer([], buffer)
    p.start(); p.join()

    send_sentinels(buffer, 1)
    c.join()

    assert dest == []


# 6. Sentinel stopping
def test_sentinel_stop():
    buffer = BlockingBuffer()
    dest = []

    c = Consumer(buffer, dest)
    c.start()

    p = Producer([1], buffer)
    p.start(); p.join()

    send_sentinels(buffer, 1)
    c.join()

    assert dest == [1]


# 7. FIFO order
def test_fifo_order():
    buffer = BlockingBuffer()
    source = list(range(20))
    dest = []

    c = Consumer(buffer, dest)
    c.start()

    p = Producer(source, buffer)
    p.start(); p.join()

    send_sentinels(buffer, 1)
    c.join()

    assert dest == source
