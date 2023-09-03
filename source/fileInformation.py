class xamlFile:
    def __init__(self,path, description, arguments):
        self.path = path
        self.description = description
        self.arguments = arguments
        
    def __str__(self) -> str:
        args = ""
        for arg in self.arguments:
            args = f'{args}\n\t{arg}'
        return f'File path: {self.path}\nDescription: {self.description}\nArguments: {args}'