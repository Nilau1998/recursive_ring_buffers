from handler.buffer_handler import RecursiveBufferHandler


if __name__ == "__main__":
    buffer_handler = RecursiveBufferHandler()

    for i in range(1000):
        buffer_handler.write_into_buffer(i)
        print(f"Value of Buffer 1: {buffer_handler.get_buffer(1).average()}")
        print(f"Value of Buffer 3: {buffer_handler.get_buffer(3).average()}")
