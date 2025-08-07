"""Ce fichier/module contient l'exercice 8."""


def log_decorator(func):
    def wrapper():
        print("Message avant l'execution du fonction")
        function_executed = func()
        print("Message après l'execution du fonction")
        return function_executed
    return wrapper
 
@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
