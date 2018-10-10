# 封装EXCEL文件的操作方法
from openpyxl import load_workbook
import time


class ParseExcel:
    def __init__(self):
        self.workbook = None
        self.excel_file = None
        self.sheet = None

    # 打开excel文件,返回文件对象
    def load_workbook(self, excel_path):
        try:
            self.workbook = load_workbook(excel_path)
        except Exception as e:
            raise e
        self.excel_file = excel_path
        return self.workbook

    # 根据sheet名获取sheet对象
    def get_sheet_by_name(self, sheet_name):
        try:
            self.sheet = self.workbook[sheet_name]
            return self.sheet
        except Exception as e:
            raise e

    # 获取结束行号
    def get_row_number(self):
        try:
            return self.sheet.max_row
        except Exception as e:
            raise e

    # 获取结束列号
    def get_cols_number(self):
        try:
            return self.sheet.max_column
        except Exception as e:
            raise e

    # 获取莫一行的数据
    def get_row_data(self, row_no):
        try:
            return self.sheet[row_no]
        except Exception as e:
            raise e

    # 获取某一列的数据
    def get_column(self, col_no):
        try:
            return self.sheet[col_no]
        except Exception as e:
            raise e

    # 根据单元格位置获取单元格的值
    def get_cell_value(self, rowNo, colsNo):
        try:
            self.cell_value = self.sheet.cell(rowNo, colsNo)
            return self.cell_Value
        except Exception as e:
            raise e

    # 保存excel文件
    def save_excel(self, excel_file):
        try:
            self.workbook.save(excel_file)
        except Exception as e:
            raise e

    # 根据单元格的坐标向单元格写入数据
    def writeCell(self, content, rowNo=None, colsNo=None):
        try:
            self.get_cell_value(rowNo, colsNo)
            self.cell_value.value = content
            self.save_excel(self.excel_file)
        except Exception as e:
            raise e

    # 写入当前时间
    def write_current_time(self, rowNo=None, colsNo=None):
        try:
            now = int(time.time())
            time_array = time.localtime(now)
            current_time = time.strftime("%Y-%m-%d%H:%M:%S", time_array)
            self.cell_value.value = current_time
            self.save_excel(self.excel_file)
        except Exception as e:
            raise e

    # 根据caseid获取整行内容
    def caseid_getrow_data(self, caseid):
        self.rownum = self.caseid_getrow_num(caseid)
        return self.getRow(self.rownum)

    # 根据caseid获取行号
    def caseid_getrow_num(self, caseid):
        rownum = 0
        self.colsdata = self.getColumn("A")
        for coldata in self.colsdata:
            if caseid == coldata.value:
                return rownum
            rownum = rownum + 1


if __name__ == '__main__':
    pe = ParseExcel()
    pe.loadWorkBook(r"..\dataconfig\testdata.xlsx")
    sheet = pe.getSheetByName('sheet1')
    print(pe.getRowNumber())
    print(pe.getColsNumber())
    print(pe.getRow(1))
    print(pe.getColumn('A'))

    print(pe.getCellOfValue(1, 2))

    print(pe.caseid_getrow_num("xxb-01"))

    print(pe.caseid_getrow_data("xxb-01"))
