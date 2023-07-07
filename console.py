from entities.bash import Bash


def parse_command(command: str, args: int):
    return command.split(" ", args)


def run():

    console = Bash()
    print("""--- Shell ---\nDebes crear un usuario y logearte, de lo contrario no podras acceder a la consola""")

    while True:
        command = input("")
        try:
            if command == 'exit':
                break

            if not (console.get_logged_in_user()):
                if command.startswith("create_user"):
                    _, username, password = parse_command(command, 2)
                    console.create_user(username, password)

                elif command.startswith("login"):
                    _, username, password = parse_command(command, 2)
                    print(console.login(username, password))

                elif command.startswith("whoami"):
                    print(console.get_logged_in_user())

            else:

                if command.startswith("create_file"):
                    _, file, content = parse_command(command, 2)
                    console.create_file(file, content)

                elif command.startswith("show"):
                    _, file = parse_command(command, 1)
                    print(console.show_file_content(file))

                elif command.startswith("metadata"):
                    _, file = parse_command(command, 1)
                    print(console.show_file_metadata(file))

                elif command.startswith("create_folder"):
                    _, folder_name = parse_command(command, 1)
                    console.create_folder(folder_name)

                elif command.startswith("cd"):
                    _, folder_name = parse_command(command, 1)
                    console.change_folder(folder_name)

                elif command.startswith("destroy_file"):
                    _, item_name = parse_command(command, 1)
                    print(console.remove_file(item_name))

                elif command.startswith("destroy_folder"):
                    _, item_name = parse_command(command, 1)
                    print(console.remove_folder(item_name))

                elif command == "ls":
                    contents = console.list_contents()
                    print("\n".join(contents))

                elif command == "whereami":
                    current_path = console.get_path()
                    print("Directorio actual:", current_path)

                elif command == "whoami":
                    logged_in_user = console.get_logged_in_user()
                    print("Usuario:", logged_in_user)

                else:
                    print("Comando invalido.")

        except ValueError as err:
            print(f"Error en la cantidad de parámetros.\n Error Message: {err}")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado.\n Error Message: {e}")


if __name__ == '__main__':
    run()
