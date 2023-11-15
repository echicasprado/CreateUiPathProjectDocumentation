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

def addHeaders(excelSheet,bold):
    bold.set_bold()
    excelSheet.write('A1','File name',bold)
    excelSheet.write('B1','File path',bold)
    excelSheet.write('C1','Description',bold)
    excelSheet.write('D1','Arguments',bold)
    return excelSheet

def addArguments(arguments):
    return ", ".join(arguments)

def getFormatCell(excelFile):
    cell_format = excelFile.add_format()
    #cell_format.set_align('center')
    #cell_format.set_align('vcenter')
    cell_format.set_border()
    cell_format.set_text_wrap()
    return cell_format
    
def getFormatHeader(excelFile):
    header_format = getFormatCell(excelFile)
    header_format.set_bold()
    header_format.set_align('center')
    header_format.set_align('vcenter')
    return header_format

def writeData(excelFile,data):
    workSheet = excelFile.add_worksheet()
    workSheet.set_column('A:D',30)
    workSheet = addHeaders(workSheet,getFormatHeader(excelFile))
    
    cell_format = getFormatCell(excelFile)
    counter = 2

    for item in data:
        workSheet.write(f'A{counter}',f'{item.fileName}',cell_format)
        workSheet.write(f'B{counter}',f'{item.path}',cell_format)
        workSheet.write(f'C{counter}',f'{item.description}',cell_format)
        workSheet.write(f'D{counter}',f'{addArguments(item.arguments)}',cell_format)
        counter = counter + 1

    return excelFile

def exportDataToExcel(rootpath,data):
    excelFile = createExcelFile(rootpath)
    excelFile = writeData(excelFile,data)
    excelFile.close()
    