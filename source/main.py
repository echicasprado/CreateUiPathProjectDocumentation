import os # use os
import glob # use to show folders and files
    
def useOS(filePath,rootFolderPath):
    currentFilePath = os.path.abspath(filePath)
    currentFilePathFromRootFolder = currentFilePath.replace(rootFolderPath, "")
    print(currentFilePathFromRootFolder)

def readFile(filePath):
    file = open(filePath,'r')
    [print(line) for line in file.readlines()]
    file.close()
    
def getAllFiles(rootFolderPath):
    rootFolder = rootFolderPath + "/**/*.*"
    print("Show tree project")
    for file in glob.glob(rootFolder, recursive=True):
        useOS(file,rootFolderPath)

def main():
    rootFolderPath = input("Ingresar ruta del proyecto: ")
    readFile(rootFolderPath)
    
if __name__ == "__main__":
    main()

# Run command to install dependecies    
# pip install -r requirements.txt