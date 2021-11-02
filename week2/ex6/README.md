# Python Virtual Environment

The Python virtual environment enables you to have a localized dependency setup for Python projects. You can create virtual environments for each project you're working on in order to keep the dependencies of those projects separate with different version numbers.

In order to use Python virtual environments, first install the python `venv` module. In ubuntu, you can install with 
```
  sudo apt install python-venv 
```

Once you have the module installed, you can run the following to create a virtual environment named `testenv` in the current folder wher your terminal is running.
```
  python -m venv testenv 
```

In order to activate this environment, you can run the following:
```
  source testenv/bin/activate
```

Once the virtual environment is activated, you'll notice that your terminal prompt is preceeded with `(testvenv) `
When you see that indicator it means that any python package you install using `pip` on that terminal will be installed to the folder you created; `testvenv`

When you want to deactivate, you can run 
```
  deactivate 
```

and you'll notice the `(testenv) ` disappear from your terminal prompt.
