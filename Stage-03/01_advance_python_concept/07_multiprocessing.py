from multiprocessing import Process

# Function that will run inside each separate process
def calculate(name):

    print(f"{name} started")

    total = 0

    # CPU-bound calculation
    for i in range(50_000):
        total += i

    print(f"{name} completed", total)


if __name__ == "__main__":

    # Create two separate processes
    process1 = Process(
        target=calculate,
        args=("Process 1",)
    )

    process2 = Process(
        target=calculate,
        args=("Process 2",)
    )

    # Start both processes
    process1.start()
    process2.start()

    # Msin process Wait for both processes to finish
    process1.join()
    process2.join()

    print("All processes completed")