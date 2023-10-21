from collections import deque


class RecursiveRingBuffer:
    def __init__(self, max_depth, buffer_size):
        self.depth = max_depth
        self.buffer_size = buffer_size
        self.buffer = deque(maxlen=buffer_size)
        self.child_buffer = self.setup_child_buffer()

        self.child_pass_counter = 0

        self.last_value_written = 0
        self.is_new_last_value = False

    def setup_child_buffer(self):
        if self.depth > 1:
            print(f"I'm at depth {self.depth}")
            return RecursiveRingBuffer(self.depth - 1, self.buffer_size)
        else:
            print(f"I'm the last buffer at depth {self.depth}")
            return None

    def write_to_bin(self, value):
        self.buffer.append(value)
        self.last_value_written = value
        self.is_new_last_value = True

        if self.child_buffer == None:
            return

        self.child_pass_counter += 1
        if self.child_pass_counter == self.buffer_size:
            self.child_buffer.write_to_bin(self.average())
            self.child_pass_counter = 0

    def average(self):
        if (len(self.buffer)) == 0:
            return 0
        else:
            return sum(self.buffer) / len(self.buffer)

    def last_written_value(self):
        if self.is_new_last_value:
            self.is_new_last_value = False
            return self.last_value_written
        else:
            return None
