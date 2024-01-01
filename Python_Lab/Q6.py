# 6.1 Write a program to implement Multithreading. Printing “Hello” with one
# thread &amp; printing “Hi” with another thread.

import threading
import time

ran=int(input("Enter the Range of Threads:"))

def hello():
    for _ in range(ran):
        time.sleep(1)
        print("Hello")

def hi():
    for _ in range(ran):
        time.sleep(1)
        print("Hi")

thread_hello = threading.Thread(target=hello)
thread_hi = threading.Thread(target=hi)

thread_hello.start()
thread_hi.start()

thread_hello.join()
thread_hi.join()

print("\nExecution completed.")
