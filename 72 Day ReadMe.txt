Day 72 -> Multithreading in python


Multithreading in Python:
Multithreading lets multiple threads (lightweight processes) run at the same time within a single program. In Python, the threading module helps us create and manage threads. 
This makes programs faster and more efficient, especially for tasks that can run in parallel.

Using the threading Module:
Before creating threads, we need to import the module.

Creating a Simple Thread: 
1. Define a function to run in the thread.
2. Create a Thread object with target=function.
3. Start the thread with start().
4. Use join() to wait for it to finish.

What is Thread Pooling:
Thread pooling is a way to reuse a fixed number of threads instead of creating new ones for each task.
The concurrent.futures.ThreadPoolExecutor module helps us run multiple tasks in parallel efficiently.

How It Works: 
1. Create a pool of threads using ThreadPoolExecutor().
2. Submit tasks to the pool with submit() or map().
3. Threads pick tasks and execute them.
4. Results are collected when tasks finish.

