# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wraper(*args):
        name = f"You called {func.__name__}{args} \nIt returned: {func(args[0],args[1],args[2])} "
        return name
    return wraper


# Use the decorator 👇
@logging_decorator
def a_function(a,b,c):
    return a * b * c

print(a_function(1,2,3))