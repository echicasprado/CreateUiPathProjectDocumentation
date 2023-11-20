from bs4 import BeautifulSoup
from source.Object.XamlFile  import XamlFile
import os

class ReadXamlFile:
    def __init__(self):
        self.FILES_TYPE_UIPATH = ["Flowchart","StateMachine","Sequence"]
        self.DESCRIPTION_UIPATH = "sap2010:Annotation.AnnotationText"
        self.ARGUMENTS_UIPATH = 'x:Property'
        self.ARGUMENT_NAME_UIPATH = 'Name'
    
    def IsvalidFile(self,filePath):
        """valid file extension

        Args:
            filePath (string): file path

        Returns:
            bool: is valid file extension
        """
        file_name, file_extension= os.path.splitext(filePath)
        
        if file_extension == ".xaml":
            return True
        else:
            return False
    
    def __openFile(self,filepath):
        """Open fiel and read xaml file

        Args:
            filepath (string): current file path

        Returns:
            string: string with xml format
        """
        with open(filepath,'r') as currentFile:
            data = currentFile.read()
        return BeautifulSoup(data,"xml")
    
    def __getDescription(self,XML_DATA):
        """_summary_

        Args:
            XML_DATA (string): xml string

        Returns:
            string: description about xaml file
        """
        for currentType in self.FILES_TYPE_UIPATH:
            currentType = XML_DATA.find(currentType)
            
            if(currentType == None):
               continue
            else:
                return currentType.get(self.DESCRIPTION_UIPATH)
        
    def __getArguments(self,XML_DATA):
        """Get all arguments from xaml file

        Args:
            XML_DATA (string): xml string

        Returns:
            string []: array with arguments into xaml file
        """
        arrayProperty = []
        currentArguments = XML_DATA.find_all(self.ARGUMENTS_UIPATH)
        
        for arg in currentArguments:
            arrayProperty.append(arg.get(self.ARGUMENT_NAME_UIPATH))
        return arrayProperty
        
    def readXamlFile(self,filePath):
        """Read current xaml file

        Args:
            filePath (string): current file path

        Returns:
            XamlFile: object with information about xaml file
        """
        XML_DATA = self.__openFile(filePath)
        return XamlFile(filePath,self.__getDescription(XML_DATA),self.__getArguments(XML_DATA),"")
    