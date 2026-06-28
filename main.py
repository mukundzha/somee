# SOMEE - SNIPPET MANAGER

def show_help():
    print("Available Commands:")
    print("add       Create a snippet")
    print("search    Find snippets")
    print("list      Show all snippets")
    print("delete    Remove a snippet")
    print("help      Show available commands")
    print("exit      Quit Somee")
    print("")


def loading_page():
    print("Somee")
    print("Your Second Brain for Code.")
    print("\nType 'help' to get started.\n")

    while True:
        command = input("somee > ").strip().lower()
        print()

        if command == "" or command == "help":
            show_help()
        elif command == "exit":
            break
        else:
            print("Invalid command.")


loading_page()