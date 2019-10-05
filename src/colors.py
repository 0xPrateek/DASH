#! /usr/bin/python

black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
white ='\033[1;37m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'
end = '\x1b[0m'

# Used for printing error message on terminal
def error(message):
    message = str(message)
    initial =red + '[-] '

    print(initial + end + message)


# Used for printing success message on terminal
def success(message):
    message = str(message)
    initial = green+'[+] '

    print(initial + end + message)


# Used for printing warning or information on terminal
def info(message):
    message = str(message)
    initial = white + '[!] '

    print(initial + end + message)


# Used for printing process related updates on terminal
def process(message):
    message=str(message)
    initial= white + '[~] '

    print(initial + end + message)
