Day 69 -> Function Caching in python


Function Caching in Python
Function caching is a method used to improve program performance by storing the results of function calls so they can be reused instead of recalculated. 
This is especially useful for functions that take significant time or resources to execute, or when inputs don’t change often.
In Python, this is done using functools.lru_cache, which caches outputs based on inputs. The maxsize parameter sets how many results to keep (or unlimited if None).
