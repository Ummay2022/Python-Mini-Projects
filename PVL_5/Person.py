class Person:
    def __init__(self, name: str):
        self.name = name
        self.children = []


    def get_name(self) -> str:
        return self.name

    def get_children(self) -> ['Person']:
        return self.children
        
