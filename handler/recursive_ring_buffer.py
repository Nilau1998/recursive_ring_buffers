from collections import deque


class RecursiveRingBuffer:
    def __init__(self, max_depth, buffer_size):
        self.depth = max_depth
        self.buffer_size = buffer_size
        self.buffer = deque(maxlen=buffer_size)
        self.child_buffer = self.setup_child_buffer()

        self.write_counter = 0

    def setup_child_buffer(self):
        if self.depth > 1:
            print(f"I'm at depth {self.depth}")
            return RecursiveRingBuffer(self.depth - 1, self.buffer_size)
        else:
            print(f"I'm the last buffer at depth {self.depth}")
            return None

    def write_to_bin(self, value):
        self.buffer.append(value)
        if self.child_buffer == None:
            return
        self.write_counter += 1
        if self.write_counter == self.buffer_size:
            print(f"Buffer {self.depth} full, writing to {self.child_buffer.depth}")
            self.child_buffer.write_to_bin(self.average())
            self.write_counter = 0

    def average(self):
        if (len(self.buffer)) == 0:
            return 0
        else:
            return sum(self.buffer) / len(self.buffer)
