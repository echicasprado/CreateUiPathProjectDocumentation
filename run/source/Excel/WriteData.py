import xlsxwriter
from source.Excel.Formats import Formats
from source.Object.XamlFile import XamlFile

class WriteData:
    def __init__(self) -> None:
        self.workBook = None
        self.workSheet = None
        self.data = None
        self.FORMATS = None
    
    def __GetFormats(self):
        self.FORMATS = Formats(self.workBook)
        
    def __addWorkSheet(self):
        self.workSheet = self.workBook.add_worksheet()
        self.workSheet.set_column('A:D',30)
    
    def __addHeaders(self):
        self.workSheet.write('A1','File name',self.FORMATS.getHeaderFormat())
        self.workSheet.write('B1','File path',self.FORMATS.getHeaderFormat())
        self.workSheet.write('C1','Description',self.FORMATS.getHeaderFormat())
        self.workSheet.write('D1','Arguments',self.FORMATS.getHeaderFormat())
     
    def __addArguments(self,arguments):
        if arguments:
            return ", ".join(arguments)
        else:
            return "N/A"
    
    def __writeCellData(self):
        counter = 2
        
        for item in self.data:
            self.workSheet.write(f'A{counter}',f'{item.fileName}',self.FORMATS.getCellFormat())
            self.workSheet.write(f'B{counter}',f'{item.path}',self.FORMATS.getCellFormat())
            self.workSheet.write(f'C{counter}',f'{item.description}',self.FORMATS.getCellFormat())
            self.workSheet.write(f'D{counter}',f'{self.__addArguments(item.arguments)}',self.FORMATS.getCellFormat())
            counter = counter + 1
    
    def WriteFile(self,workBook,data):
        self.workBook = workBook
        self.data = data
        self.__GetFormats()
        self.__addWorkSheet()
        self.__addHeaders()
        self.__writeCellData()