import os
import glob
from source.ReadXamlFile import ReadXamlFile
from source.ExportData import ExportData

class WorkWithProject:
    
    def __init__(self,rootFolderProject):
        """constructor work with project

        Args:
            rootFolderProject (string): folder project path
        """
        self.rootFolderProject = rootFolderProject
        self.projectInformation = None
        self.exportData = ExportData()
        self.readFile = ReadXamlFile()
    
    def work(self):
        """work with current project"""
        self.projectInformation = self.__getAllFiles()
        self.exportData.exporData(self.rootFolderProject,self.projectInformation)
        self.__showProjectInformation()
        
    
    def __getRelavitePath(self,filePath):
        """Get relative path from file path, this function use root folder project path

        Args:
            filePath (string): current file path

        Returns:
            string: relative path from current path
        """
        currentFilePath = os.path.abspath(filePath)
        return currentFilePath.replace(self.rootFolderProject, "")
    
    def __getAllFiles(self):
        """Get information about all files in the project

        Returns:
            XamlFile[]: return XamlFile(obj) array with information files
        """
        ArrayFiles = []
        rootFolder = self.rootFolderProject + "/**/*.*"
    
        for file in glob.glob(rootFolder, recursive=True):
            isValidFile = self.readFile.IsvalidFile(file)
            
            if isValidFile:
                currentFileObject = self.readFile.readXamlFile(file)
                currentFileObject.fileName = self.__getRelavitePath(file)
                ArrayFiles.append(currentFileObject)
            
        return ArrayFiles
    
    def __showProjectInformation(self):
        """Show all information about project
        """
        for file in self.projectInformation:
            print(str(file))
            print('####################################')
    