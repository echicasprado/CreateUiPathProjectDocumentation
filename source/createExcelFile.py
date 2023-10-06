import xlsxwriter
import os

def isExistsExcelFile(path):
    if os.path.exists(path):
        print(f'The file: {path} exist, remove de current file')
        os.remove(f'{path}')
    else:
        print(f'The file: {path} no exist')

def createExcelFile(folderPath):
    excelPath = f'{folderPath}/table.xlsx'
    isExistsExcelFile(excelPath)
    return xlsxwriter.Workbook(f'{excelPath}')

def addHeaders(excelSheet):
    excelSheet.write('A1','File name')
    excelSheet.write('B1','File path')
    excelSheet.write('C1','Description')
    excelSheet.write('D1','Arguments')
    return excelSheet

def addArguments(arguments):
    return ", ".join(arguments)

def writeData(excelFile,data):
    workSheet = excelFile.add_worksheet()
    workSheet = addHeaders(workSheet)
    
    counter = 2

    for item in data:
        workSheet.write(f'A{counter}',f'{item.fileName}')
        workSheet.write(f'B{counter}',f'{item.path}')
        workSheet.write(f'C{counter}',f'{item.description}')
        workSheet.write(f'D{counter}',f'{addArguments(item.arguments)}')
        counter = counter + 1

    return excelFile

def exportDataToExcel(rootpath,data):
    excelFile = createExcelFile(rootpath)
    excelFile = writeData(excelFile,data)
    excelFile.close()
    