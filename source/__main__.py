import os # use os
import glob # use to show folders and files
from readXaml import readXamlFile
    
def useOS(filePath,rootFolderPath):
    currentFilePath = os.path.abspath(filePath)
    return currentFilePath.replace(rootFolderPath, "")
    
def getAllFiles(rootFolderPath):
    ArrayFiles = []
    rootFolder = rootFolderPath + "/**/*.*"
    
    for file in glob.glob(rootFolder, recursive=True):
        currentFileObject = readXamlFile(file)
        currentFileObject.fileName = useOS(file,rootFolderPath)
        ArrayFiles.append(currentFileObject)
    return ArrayFiles

def main():
    rootFolderPath = input("Ingresar ruta del proyecto: ")
    Files = getAllFiles(rootFolderPath)
    
    for file in Files:
        print(str(file))
        print("#################################")
    
if __name__ == "__main__":
    main()