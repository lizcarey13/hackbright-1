## What is `if __name__ == '__main__'`

```python
if __name__ == '__main__':
    # Run your main execution flow here
```

This magic block of code we need to add at the end of the python file has a special purpose depends on how the file is being run.  There are two ways of using a python file: standalone program, and reusable module.

### Standalone Program
So far we only talked about running a python file directly by calling `python <file>.py` in the terminal.  When we run a file like so, we are running <file>.py as a *standalone program*.  When we run <file>.py, Python will make this special variable `__name__` for the file and assign it with the string value `__main__`.  Note that, Python makes `__name__` for EACH file:
```python
__name__ = '__main__'
```

This will make the condition of the magic block equals to `True`, which means that it will run whatever is inside the if-block, in this case, the main execution flow you specified inside.  Please note that, we mentioned you should use `main()` inside the if-block.  You do not have to.  You can put any code inside, but `main()` is a convention that developers would understand as "main execution flow".

For illustration purposes, `a.py` is created for you to explore.  If you run `a.py` on the terminal:
```shell
python a.py
```

You will see the following line printed out:
```shell
a.py: __name__ = __main__
a.py: execution_flow
a.py: function_one
```

Python executes the file from top to bottom, and it assigns `__name__` for `a.py` with the string value `__main__` here, which means it passes the condition, and it runs whatever is in the if-block.

### Reusable Module
Later you will learn about using python file as a *reusable module* where you will *import* this file/module into another file for use.  As your program gets bigger, you will start dividing up your program into number of files.  You may want to use some functions/classes/constants from a file, but you don't want to run the main execution flow in that file.  In this case, the magic block of code will help prevent Python from running the main execution flow from that file.

When you are importing a file, `__name__` for that file will now be equal to a string of the name of the file, which means it will not pass the if-condition.  As a result, it doesn't run the main execution flow.
```python
__name__ = '<file name>'
```

For illustration purposes, `b.py` is created for you to explore.  `b.py` is your standalone program, and it imports `a.py`.  So `b.py` can use the functions inside `a.py`.

If you run `b.py` on the terminal:
```shell
python b.py
```

You will see the following line printed out:
```shell
a.py: __name__ = a
b.py: __name__ = __main__
b.py: b_flow
b.py: b_function
a.py: function_one
```

Python runs from top to bottom.  So when it first encounters the line `import a`.  It will find `a.py` in the directory, and execute it line by line.  You can see that `__name__` for `a.py` is now the string `a`, which is the name of the file, instead of the string `__main__`.  This is because `a.py` is now the reusable module, and not the standalone program.  Therefore, the if-condition in `a.py` did not pass, and it did not run `execute_flow` of `a.py`.

But on the other hand, `b.py`'s `__name__` variable is `__main__`.  This is because we are running `b.py` as a standalone program.  And it means it passes the if-condition, and it runs `b_flow`.