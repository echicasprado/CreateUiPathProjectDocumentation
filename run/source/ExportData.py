from source.Excel.CreateExcelFile import CreateExcelFile
from source.Excel.WriteData import WriteData
import xlsxwriter

class ExportData:
    def __init__(self) -> None:
        pass
    
    def exporData(self,rootFolderPath,data):
        writeExcelFile = WriteData()
        createExcel = CreateExcelFile(rootFolderPath)
        excelFile = createExcel.createNewExcelFile()
        writeExcelFile.WriteFile(excelFile,data)
        excelFile.close()