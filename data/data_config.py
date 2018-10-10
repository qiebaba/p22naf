# 定义全局变量
import os

# 当前文件所在目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据文件存放路径
dataFilePath = parentDirPath+u"\\dataconfig\\testdata.xlsx"

# 配置文件存放路径
confFilePath = parentDirPath+r"\dataconfig\conf.ini"

# sheet名
sheetName = 'sheet1'

Id = 1
request_name = 2
url = 3
run = 4
request_way = 5
header = 6
case_depend = 7
data_depend = 8
field_depend = 9
data = 10
expect = 11
result = 12


