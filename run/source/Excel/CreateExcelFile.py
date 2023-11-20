import xlsxwriter
import os

class CreateExcelFile:
    def __init__(self,rootFolderPath):
        self.rootFolderPath = rootFolderPath
    
    def __isExistsExcelFile(self,filePath):
        """Is exists current excel file

        Args:
            filePath (string): current file path
        """
        if os.path.exists(filePath):
            print(f'The file: {filePath} exist, remove de current file')
            os.remove(filePath)
        else:
            print(f'The file: {filePath} no exist')    
    
    def createNewExcelFile(self):
        """create excel file

        Returns:
            Workbook: new workbook
        """
        excelPath = f'{self.rootFolderPath}/table.xlsx'
        self.__isExistsExcelFile(excelPath)
        return xlsxwriter.Workbook(excelPath) 