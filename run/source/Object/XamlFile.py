class XamlFile:
    def __init__(self,path, description, arguments,fileName):
        self.path = path
        self.description = description
        self.arguments = arguments
        self.fileName = fileName
    
    def getPath(self):
        return self.path
    
    def getDescription(self):
        return self.description
    
    def getArguments(self):
        return self.arguments
    
    def getFileName(self):
        return self.fileNames
    
    def __str__(self) -> str:
        args = ""
        for arg in self.arguments:
            args = f'{args}\n\t{arg}'
        return f'File name: {self.fileName}\nFile path: {self.path}\nDescription: {self.description}\nArguments: {args}'