# Licensed under the GNU AGPL 3.0
# Source code available at https://github.com/commma-tose/PY-DOS/
# Version alpha-0.1

import platform

pydosversion = "alpha-0.1" # Easy way to change the output for the "version" command.

def pydos_debug(): # This took way too long to make

    print("PY-DOS Version:", pydosversion)
    print("Architecture:", platform.architecture())
    print("Machine:", platform.machine())
    print("Node:", platform.node())
    print("Platform:", platform.machine())
    print("Processor:", platform.processor())
    print("Python Build:", platform.python_build())
    print("Python Compiler:", platform.python_compiler())
    print("Python Branch:", platform.python_branch())
    print("Python Implementation:", platform.python_implementation())
    print("Python Revision:", platform.python_revision())
    print("Python Version:", platform.python_version())
    print("Python Version Tuple:", platform.python_version_tuple())
    print("Release:", platform.release())
    print("System:", platform.system())
    print("Version:", platform.version())
    print("Uname:", platform.uname())

while True: # Loop

    user_command = input("Command: ") # Initial command prompt

    # The following if command is a mess, you have been warned.

    if user_command == "help": # Command: help
        print("All commands are case-sensitive and lowercase.\nhelp: Show this screen again\ninfo: Show information.\ndebug: Show debug info\nexit: Quit PY-DOS") # This is gonna be so fucking fun to maintain as I add new commands
    else:
        if user_command == "info": # Command: info
            print("PY-DOS by Commatose, licensed under the AGPL 3.0. Version", pydosversion)
        else:
            if user_command == "debug": # Command: debug
                    pydos_debug()
            else:
                if user_command == "exit": # Command: exit
                    exit()
                else:
                    print("Bad command, try typing\"help\"") # Give error if command doesn't exist

