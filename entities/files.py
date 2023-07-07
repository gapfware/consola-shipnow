class File:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content
        self.metadata = {}

    def show_content(self):
        return self.content

    def show_metadata(self):
        return self.metadata
