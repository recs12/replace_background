""" Replace background with the official of the company.
"""

from System.IO.Path import Combine
import System.Runtime.InteropServices as SRI
from System import Console
import System
import sys
import clr
import replace

clr.AddReference("System")
clr.AddReference("System.IO")
clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

__project__ = "ReplaceBackground"
__author__ = "recs"
__version__ = "0.0.1"
__update__ = "2020-10-30"


def prompt_exit():
    raw_input("\nPress any key to exit...")
    sys.exit()


def confirmation(func):
    response = raw_input(
        """Would you like to update the background, (Press y/[Y] to proceed.):\n>""")
    if response.lower() in ["y"]:
        func()
        prompt_exit()
    elif response in ["*"]:
        func()
    else:
        sys.exit()


def raw_input(message):
    Console.WriteLine(message)
    return Console.ReadLine()


def username():
    return System.Environment.UserName


def main():

    try:
        application = SRI.Marshal.GetActiveObject("SolidEdge.Application")
        response = raw_input(
            """Would you like to update the background, (Press y/[Y] to proceed.):\n"(Option: Press '*' for processing documents in batch)""")

        if response.lower() in ["y", "yes"]:
            doc = application.ActiveDocument
            replace.background(doc)
        elif response.lower() in ["*"]:
            # loop through all the drafts
            documents = application.Documents
            for doc in documents:
                replace.background(doc)
        else:
            pass

    finally:
        prompt_exit()


if __name__ == "__main__":
    print("%s\n--author: %s --version: %s --last-update : %s \n" %
          (__project__, __author__, __version__, __update__))
    main()
