import sys

def run(source: str):
    print(source)
    print("Error: Scanner Not Implemented", file=sys.stderr)


def run_file(path: str):
    with open (path, "r") as f:
        source = f.read()
    run(source)

def run_prompt():
    while True:
        try:
            line = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            print("Exiting...")
            break
        run(line)


def main():
    args = sys.argv[1:]

    if len(args) > 1:
        print("Usage: lox.py [script]")
        sys.exit(64)
    elif len(args) == 1:
        run_file(args[0])
    else:
        run_prompt()

if __name__ == "__main__":
    main()
