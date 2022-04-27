# Make a class called Counter, and make it a subclass of the Thread class in the Threading module.
# Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000.
# Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times)
# and for each time increments the value of the counter by 1. Create 2 instances of the thread and start them,
# then join them and check the result of the counter, it should be 200.000, right? Run it a couple of times
# and consider some different reasons why you get the answer that you get.
import threading
from threading import Thread


class Counter(Thread):
    count = 0
    rounds = range(100000)

    def run(self):
        for c in self.rounds:
            self.count += 1
        print(self.count)

def main():
    threads_list = []
    counter = Counter()
    counter_2 = Counter()

    thread = threading.Thread(target=counter.run)
    thread_2 = threading.Thread(target=counter_2.run)
    threads_list.append(thread)
    thread.start()
    threads_list.append(thread_2)
    thread_2.start()
    for thread in threads_list:
        thread.join()


if __name__ == '__main__':
    main()
