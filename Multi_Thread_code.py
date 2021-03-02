import operator
import random
import threading
from datetime import datetime


def operator_selection():
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    for i in range(500):
        num_1 = random.randint(1, 20)
        num_2 = random.randint(1, 20)
        op, fn = random.choice(operators)
        print("{} {} {} = {}".format(num_1, op, num_2, fn(num_1, num_2)))


if __name__ == "__main__":
    start_time = datetime.now()
    # Creating thread
    thread_1 = threading.Thread(target=operator_selection(), args=None)
    # Starting thread
    thread_1.start()
    print("Multi Threading Task completed")
    end_time = datetime.now()

print("Duration of multithread operation is {}:".format(end_time - start_time))
