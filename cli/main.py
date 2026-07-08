import sys
from commands.show import ShowCommand
from commands.add import AddCommand
from commands.extract import ExtractCommand


COMMANDS = {
    "show": ShowCommand(),
    "add": AddCommand(),
    "extract": ExtractCommand()
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [args]")
        print("Commands:")
        print("  show            List all movies")
        print("  add <title>     Add a new movie")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    handler = COMMANDS.get(command)
    if not handler:
        print(f"Unknown command: {command}")
        return

    handler.execute(args)

if __name__ == "__main__":
    main()