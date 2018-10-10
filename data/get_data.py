from util.operation_excel import ParseExcel
from data import data_config
from util.operation_json import OperetionJson
#from util.connect_db import OperationMysql
class GetData:
	def __init__(self):
		#实例化数据库操作，数据配置
		self.opera_excel = ParseExcel()
		self.data =data_config
		#获取workbook对象和sheet对象
		self.opera_excel.loadWorkBook(self.data.dataFilePath)
		self.sheet = self.opera_excel.getSheetByName(self.data.sheetName)


	#去获取excel行数,就是我们的case个数	
	def get_case_lines(self):
		try:
			case_lines = self.opera_excel.getRowNumber(self.sheet)
			return case_lines
		except Exception as e:
			raise e

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		run_model = self.opera_excel.getCellOfValue(self.sheet,row,self.data.run)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	#是否携带header
	def is_header(self,row):

		header = self.opera_excel.getCellOfValue(self.sheet,row,self.data.header)
		if header != '':
			return header
		else:
			return None

	#获取请求方式
	def get_request_method(self,row):
		try:
			request_method = self.opera_excel.getCellOfValue(self.sheet,row,self.data.request_way)
			return request_method
		except Exception as e:
			raise e

	#获取url
	def get_request_url(self,row):
		try:
			url = self.opera_excel.getCellOfValue(self.sheet,row,self.data.url)
			return url
		except Exception as e:
			raise e

	#获取请求数据
	def get_request_data(self,row):
		data = self.opera_excel.getCellOfValue(self.sheet,row,self.data.data)
		if data == '':
			return None
		return data

	#通过获取关键字拿到data数据
	def get_data_for_json(self,row):
		opera_json = OperetionJson()
		request_data = opera_json.get_data(self.get_request_data(row))
		return request_data

	#获取预期结果
	def get_expcet_data(self,row):
		expect = self.opera_excel.getCellOfValue(self.sheet,row,self.data.expect)
		if expect == '':
			return None
		return expect

	#通过sql获取预期结果
	def get_expcet_data_for_mysql(self,row):
		op_mysql = OperationMysql()
		sql = self.get_expcet_data(row)
		res = op_mysql.search_one(sql)
		return res.decode('unicode-escape')

	def write_result(self,row,value,colsnum):
		self.opera_excel.writeCell(self.sheet,value,row,colsnum)

	#获取依赖数据的key
	def get_depend_key(self,row):

		depent_key = self.opera_excel.getCellOfValue(self.sheet,row,8)
		if depent_key == "":
			return None
		else:
			return depent_key

	#判断是否有case依赖
	def is_depend(self,row):

		depend_case_id = self.opera_excel.getCellOfValue(self.sheet,row,7)
		if depend_case_id == "":
			return None
		else:
			return depend_case_id

	#获取数据依赖字段
	def get_depend_field(self,row):
		data = self.opera_excel.getCellOfValue(self.sheet,row,9)
		if data == "":
			return None
		else:
			return data