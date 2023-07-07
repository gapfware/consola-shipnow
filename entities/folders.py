from .files import File


class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.contents = []

    def add_folder(self, folder):
        """Crea un directorio dentro del directorio actual."""
        self.contents.append(folder)

    def add_file(self, file):
        """Agrega un archivo al directorio actual."""
        self.contents.append(file)

    def remove_folder(self, folder_name):
        for item in self.contents:
            if isinstance(item, Folder) and item.name == folder_name:
                self.contents.remove(item)
                return True
        return False

    def remove_file(self, filename):

        for item in self.contents:
            if isinstance(item, File) and item.name == filename:
                self.contents.remove(item)
                return True
        return False

    def get_contents(self):
        """Lista el contenido del directorio actual."""
        return self.contents
        # print("--- Contenido del directorio --- ")
        # for item in self.contents:
        #     if (isinstance(item, Folder)):
        #         print(f"/{item.name}")
        #     else:
        #         print(f"{item.name}")
