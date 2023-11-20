import xlsxwriter

class Formats:
    def __init__(self,excelFile):
        self.excelFile = excelFile
        self.__CELL_FORMAT = self.__setFormatCell()
        self.__HEADER_FORMAT = self.__setFormatHeader()
        
    def __setFormatCell(self):
        """set cell format 

        Returns:
            Excel_Format: format to use into cells
        """
        cell_format = self.excelFile.add_format()
        cell_format.set_border()
        cell_format.set_text_wrap()
        return cell_format
    
    def __setFormatHeader(self):
        """set header format

        Returns:
            Excel_Format: format to use into headers
        """
        header_format = self.__setFormatCell()
        header_format.set_bold()
        header_format.set_align('center')
        header_format.set_align('vcenter')
        return header_format
    
    def getCellFormat(self):
        return self.__CELL_FORMAT
    
    def getHeaderFormat(self):
        return self.__HEADER_FORMAT