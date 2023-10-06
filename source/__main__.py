import os # use os
import glob # use to show folders and files
from readXaml import readXamlFile
from createExcelFile import exportDataToExcel

# TODO Create object to use information about path files    

def useOS(filePath,rootFolderPath):
    """Fuction to get relative path with full filepath, use folderpath"""
    currentFilePath = os.path.abspath(filePath)
    return currentFilePath.replace(rootFolderPath, "")

useOS.__doc__ = "Get relative path of file, need filepath, and folderpath"
    
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
    exportDataToExcel(rootFolderPath,Files)
    
    for file in Files:
        print(str(file))
        print("#################################")
    
if __name__ == "__main__":
    main()