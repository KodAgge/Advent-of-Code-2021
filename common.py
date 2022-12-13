import inspect


def load_file(test = False):
    day = inspect.getmodule(inspect.stack()[1][0]).__file__.split("\\")[-1].split(".")[0]
    with open(f"inputs/{day}.{'test' if test else 'in'}") as file:
        return file.readlines()