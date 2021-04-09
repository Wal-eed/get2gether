"""
    A suite of global functions for debugging
"""
import json
from Get2Gether.utils.colourisation import printColoured 

def pretty(d, indent=1):
    """ Pretty print a dictionary """
    for key, value in d.items():
        printColoured('\t' * indent + str(key) + ":", colour="yellow")
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            printColoured('\t' * (indent+1) + str(value), colour="blue")

def print_pretty_json(struct, colour="yellow"):
    printColoured(json.dumps(struct, indent=4, sort_keys=True), colour=colour)
