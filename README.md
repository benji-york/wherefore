Wherefore
=========

Trace down the origin of any value in your Python application.


Command-line usage
==================

If you want to use wherefore on your entire program and your program has a
standard shebang line, you can run it from the command line, like so:

    $ wherefore 42 program.py

This will run your program and every time the target value is assigned to a
variable, assigned to a dictionary, added to a list, or returned from a
function or method, the file name and line number will be reported on stderr.

If the target value is a string it must be double-quoted, once for the shell
and once for Python.

    $ wherefore "'target value'" program.py

If you want the report sent to a file instead of stderr you can provide the -o
switch, thusly:

    $ wherefore -o report_file "'target value'" program.py


Decorator usage
===============

If, instead, you want to use wherefore on only a subset of your software, you
can use the decorator form:

    @wherefore('target value')
    def my_function():
        ...

The code inside the decorated function and any functions it calls will be
watched for the target value and it will be reported whenever it appears.

If you do not want the results sent to stderr you can provide a list and tuples
of (file_name, line_number) will be appended to it instead.

    whys_and_wherefores = []

    @wherefore('target value', whys_and_wherefores)
    def my_function():
        ...
