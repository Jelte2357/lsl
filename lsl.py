from rich import print
import sys
import os
import argparse
from pathlib import WindowsPath, Path

def main():
    parser = argparse.ArgumentParser(add_help=False)
    #parser.add_argument("-m", "--menu", action="store_true") will add at a later date
    parser.add_argument("-s", "--sorted", action="store_true")
    parser.add_argument("location", type=str, nargs="?", default=None)
    args = parser.parse_args()
    if args.location:
        args.location = args.location.lstrip("/")
    
    try:
        items = os.listdir(args.location)
    except WindowsError:
        if args.location in os.listdir() and not os.path.isdir(args.location):
            print(args.location)
            sys.exit()
        print(f"Cannot access '{args.location}': No such file or directory")
        sys.exit(1)
        
    if args.sorted:
        if args.location:
            folders = [item for item in items if os.path.isdir(os.path.join(args.location, item))]
            files = [item for item in items if not os.path.isdir(os.path.join(args.location, item))]
        else:
            folders = [item for item in items if os.path.isdir(item)]
            files = [item for item in items if not os.path.isdir(item)]  
        items = folders + files
    
    for item in items:
        if args.location:
            if os.path.isdir(os.path.join(args.location, item)):
                print(f"[u blue link={Path(os.path.join(args.location, item)).absolute().as_uri()}]{item}[/u blue link]")
            else:
                print(f"[link={Path(os.path.join(args.location, item)).absolute().as_uri()}]{item}[/link]")
        
        else:
            if os.path.isdir(item):
                print(f"[u blue link={Path(item).absolute().as_uri()}]{item}[/u blue link]")
            else:
                print(f"[link={Path(item).absolute().as_uri()}]{item}[/link]")

main()