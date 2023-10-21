from handler.buffer_handler import RecursiveBufferHandler

import matplotlib.pyplot as plt
import random

if __name__ == "__main__":
    buffer_handler = RecursiveBufferHandler(max_depth=5)

    buf_1 = []
    buf_2 = []
    buf_3 = []
    buf_5 = []
    buf_4 = []

    for i in range(100000):
        buffer_handler.write_into_buffer(random.randint(0, 100))

        last_buf_5_value = buffer_handler.get_buffer(5).last_written_value()
        if last_buf_5_value != None:
            buf_5.append(last_buf_5_value)

        last_buf_4_value = buffer_handler.get_buffer(4).last_written_value()
        if last_buf_4_value != None:
            buf_4.append(last_buf_4_value)

        last_buf_3_value = buffer_handler.get_buffer(3).last_written_value()
        if last_buf_3_value != None:
            buf_3.append(last_buf_3_value)

        last_buf_2_value = buffer_handler.get_buffer(2).last_written_value()
        if last_buf_2_value != None:
            buf_2.append(last_buf_2_value)

        buffer_1 = buffer_handler.get_buffer(1)
        last_buf_1_value = buffer_handler.get_buffer(1).last_written_value()
        if last_buf_1_value != None:
            buf_1.append(last_buf_1_value)

    fig, axs = plt.subplots(5)
    axs[0].plot(range(len(buf_1)), buf_1, label="Buf_1", color="blue")
    axs[1].plot(range(len(buf_2)), buf_2, label="Buf_2", color="orange")
    axs[2].plot(range(len(buf_3)), buf_3, label="Buf_3", color="green")
    axs[3].plot(range(len(buf_4)), buf_4, label="Buf_4", color="red")
    axs[4].plot(range(len(buf_5)), buf_5, label="Buf_5", color="pink")
    fig.legend()
    fig.savefig("fun.png")
