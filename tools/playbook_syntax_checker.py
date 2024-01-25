#!/bin/python3

from colorama import Style, Fore, Back
from sys import argv
from yaml import safe_load, YAMLError
from os.path import isfile

if "__main__" == __name__:
    # Remove program name
    argv = argv[1:]

    if len(argv) == 0:
        print(f"{Fore.GREEN}This tool is used to check and verify if playbooks have correct yml formatting{Style.RESET_ALL}")
        print("USAGE:")
        print(f"\t{Fore.CYAN}python3 playbook_syntax_checker.py <playbook_path>{Style.RESET_ALL}")
        exit(1)
    elif isfile(argv[0]):
                
        print(f"{Fore.BLUE}INFO{Style.RESET_ALL} - Processing {argv[0]} ... ", end="")
        try:
            with open(argv[0], mode="r") as playbook_stream:
                safe_load(playbook_stream)
                print(f"{Fore.GREEN}OK{Style.RESET_ALL}")
                exit(0)
        except YAMLError as e:
            print()
            print(f"{Fore.RED}ERROR{Style.RESET_ALL} - {Fore.YELLOW}The file {argv[0]} has not a correct yml syntax{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{e}{Style.RESET_ALL}")
            exit(2)
    else:
        print(f"ERROR - File {argv[0]} does not exist.")
        exit(3)