class xamlFile:
    def __init__(self,path, description, arguments,fileName):
        self.path = path
        self.description = description
        self.arguments = arguments
        self.fileName = fileName
        
    def __str__(self) -> str:
        args = ""
        for arg in self.arguments:
            args = f'{args}\n\t{arg}'
        return f'File name: {self.fileName}\nFile path: {self.path}\nDescription: {self.description}\nArguments: {args}'