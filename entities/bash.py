from .folders import Folder
from .files import File
from .users import User
from datetime import datetime


class Bash:
    def __init__(self) -> None:
        self.root_folder = Folder("root")
        self.logged_in_user = None
        self.current_folder = self.root_folder
        self.users = []

    def create_file(self, filename, content):
        new_file = File(filename, content)
        new_file.metadata = {
            "Created by": self.get_logged_in_user(),
            "Created on": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "size": f"{new_file.__sizeof__()} bytes"
        }
        self.current_folder.add_file(new_file)

    def show_file_content(self, filename):
        for item in self.current_folder.get_contents():
            if isinstance(item, File) and item.name == filename:
                return item.show_content()
            else:
                return "Archivo no encontrado."

    def show_file_metadata(self, filename):
        for item in self.current_folder.get_contents():
            if isinstance(item, File) and item.name == filename:
                return item.metadata

    def create_folder(self, folder_name):
        new_folder = Folder(folder_name)
        self.current_folder.add_folder(new_folder)

    def change_folder(self, folder_name):
        if folder_name == "..":
            if self.current_folder.parent:
                self.current_folder = self.current_folder.parent
                return
            else:
                return "Ya se encuentra en el directorio raíz."
        else:
            for item in self.current_folder.get_contents():
                if isinstance(item, Folder) and item.name == folder_name:
                    self.current_folder = item
                    return
            return "Directorio no encontrado."

    def remove_file(self, filename):
        if not (self.current_folder.remove_file(filename)):
            return "Archivo no encontrado."
        else:
            return "Archivo eliminado con éxito."

    def remove_folder(self, folder_name):
        if not (self.current_folder.remove_folder(folder_name)):
            return "Directorio no encontrado."
        else:
            return "Directorio eliminado con éxito."

    def list_contents(self):
        contents = []
        for item in self.current_folder.get_contents():
            if isinstance(item, File):
                contents.append(f"File: {item.name}")
            elif isinstance(item, Folder):
                contents.append(f"Folder: /{item.name}")
        return contents

    def get_path(self):
        path = []
        current = self.current_folder
        while current is not None:
            path.insert(0, current.name)
            current = current.parent
        return "/" + "/".join(path)

    def create_user(self, username, password):
        new_user = User(username, password)
        print(f"Usuario: {username} creado con éxito.")
        self.users.append(new_user)

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.get_password() == password:
                self.logged_in_user = user
                return "Ha iniciado sesión con éxito."
        return "Nombre de usuario o contraseña inválido."

    def get_logged_in_user(self):
        if self.logged_in_user:
            return self.logged_in_user.username
