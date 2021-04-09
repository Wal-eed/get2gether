from colored import stylize, fg
import shutil

def printBorder():
    """
        Prints a border exactly equal to the current terminal instance"s width
    """
    terminal_dim = shutil.get_terminal_size((80, 20))
    print("╠", end="")
    for i in range(1, terminal_dim.columns - 1):
        print("═", end="")
    print("╣")

def printColoured(*args, bordersOn=False, colour="green", **kwargs):
    if bordersOn:
        printBorder()
    try:
        print(stylize(" ".join(map(str, args)), fg(colour)), **kwargs)
    except:
        print(args)
    if bordersOn:
        printBorder()
