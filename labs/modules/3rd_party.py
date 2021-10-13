from termcolor import colored
import pyfiglet

print(colored(
    "It works!", "red"
))

print(colored(
    "It works!", "red", attrs=["bold", "underline"]
))

print(pyfiglet.figlet_format("IT works!", font="isometric1"))