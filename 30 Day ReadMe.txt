Day 37 -> Finally keyword


finally Keyword: 
The finally block is used in exception handling to define code that must run no matter what—whether an error occurs or not.
It’s useful for cleanup actions, like closing files, releasing resources, or ending a process.
One of the important use cases of finally block is in a function which returns a value.
Many people has this confusion why use fianlly when we can just simply write our statement in print , but when you are returing a function it will happen that you use simple print , it will not be executed due to return statement , cause we know a function stops when it meets any returning keyword , but in case of finally it will not happen , and the statement inside the finally will be executed , even there is a return keyword . 