# SOMEE - SNIPPET MANAGER

Title = []
Language = []
Description = []
Code = []

print()


def show_help():
    print("Available Commands:")
    print("add       Create a snippet")
    print("search    Find snippets")
    print("list      Show all snippets")
    print("delete    Remove a snippet")
    print("help      Show available commands")
    print("exit      Quit Somee")
    print()


def add_ask():
    global Title
    global Language
    global Description
    global Code

    title = input("Title: ")
    language = input("Language: ")
    description = input("Description: ")
    print("")
    print("Code (type 'END' on a new line to finish):")
    print("")
    code_lines = []

    while True:
        line = input()

        if line == "END":
            break

        code_lines.append(line)

    code = "\n".join(code_lines)

    Title.append(title)
    Language.append(language)
    Description.append(description)
    Code.append(code)

    print()
    print(f"✓ Snippet '{title}' added successfully!")
    print()


def listing_elements():
    global Title
    global Language
    global Description
    global Code

    if len(Title) == 0:
        print("No snippets found.\n")
        return

    for i in range(len(Title)):
        print(f"Snippet #{i + 1}")
        print("")
        print(f"Title       : {Title[i]}")
        print(f"Language    : {Language[i]}")
        print(f"Description : {Description[i]}")
        print("Code:")
        print(Code[i])
        print("-" * 40)
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
        elif command == "add":
            add_ask()
        elif command == "list":
            listing_elements()
        elif command == "search":
            print("Coming soon.\n")
        elif command == "delete":
            print("Coming soon.\n")
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command.\n")


loading_page()