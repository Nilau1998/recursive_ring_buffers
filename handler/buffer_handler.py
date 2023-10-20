from handler.recursive_ring_buffer import RecursiveRingBuffer


class RecursiveBufferHandler:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth
        self.buffer = RecursiveRingBuffer(3, 10)

    def write_into_buffer(self, value):
        self.buffer.write_to_bin(value)

    def get_buffer(self, depth):
        if depth == self.max_depth:
            return self.buffer

        wanted_buffer = self.buffer
        for i in range(depth - 1):
            wanted_buffer = wanted_buffer.child_buffer
        return wanted_buffer
