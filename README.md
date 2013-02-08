Wherefore
=========

Trace down the origin of any value in your Python app with Wherefore.


Basic usage
===========

If you want to use wherefore on your entire program and your program has a
standard shebang line, you can run it from the command line, like so:

    $ wherefore 42 program.py

This will run your program and every time the target value is assigned to a
variable, assigned to a dictionary, added to a list, or returned from a
function or method, the file name and line number will be reported on stderr.


Decorator usage
===============

If, instead, you want to use wherefore on only a subset of your software, you
can use the decorator form:

    @wherefore('target value')
    def my_function():
        ...

The code inside the decorated function and the code inside any function it
calls will be watched for the target value and it will be reported whenever it
appears.
