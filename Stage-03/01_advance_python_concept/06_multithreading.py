from threading import Thread
import time


# ============================================================
# 1. Creating threads using classes
# ============================================================

class Hello(Thread):
    def run(self):
        # run() contains the work performed by this thread
        for i in range(5):
            print("Hello", i + 1)
            time.sleep(0.2)


class Hi(Thread):
    def run(self):
        # run() contains the work performed by this thread
        for i in range(5):
            print("Hi", i + 1)
            time.sleep(0.2)


def main1():
    print("---------Using class with thread------")

    # Create two Thread objects
    t1 = Hello()
    t2 = Hi()

    # start() starts the thread and internally calls run()
    t1.start()
    t2.start()

    # join() makes the main thread wait for these threads
    t1.join()
    t2.join()

    print("Main thread waits for created threads because of join().")


# ============================================================
# 2. Creating threads using target function
# ============================================================

def task_t(task):
    print(task, "Started")
    time.sleep(0.1)
    print(task, "ended")


thread_list = []


def main2():
    print("main 2 started")

    list = ['task1', 'task2', 'task3']

    # Create Thread objects and store them in a list
    for i in range(len(list)):
        thread = Thread(
            target=task_t,
            args=(list[i],)         #args must in tuple
        )
        thread_list.append(thread)

    # Start all created threads
    for thread in thread_list:
        thread.start()

    # Main thread does not wait here because join() is not used
    print("Main thread runs with created threads; it does not wait to complete.")


# ============================================================
# Program entry point
# ============================================================

if __name__ == "__main__":
    main1()
    main2()