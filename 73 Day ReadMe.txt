Day 73 -> MultiProcessing in python


What is Multiprocessing:
Multiprocessing lets you run multiple processes in parallel, each with its own memory space.
It uses multiple CPU cores to speed up programs, especially for CPU-bound tasks (heavy calculations).

Using the multiprocessing Module:
Before creating processes, import the module.

Creating a Simple Process:
Define a function to run.
Create a Process object with target=function.
Start it using start().
Use join() to wait for it to finish.

