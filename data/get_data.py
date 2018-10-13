from util.operation_excel import ParseExcel
from data import data_config
from util.operation_json import OperetionJson
#from util.connect_db import OperationMysql
class GetData:
	def __init__(self):
		#实例化数据库操作，数据配置
		self.opera_excel = ParseExcel()
		self.data =data_config
		# 获取workbook对象和sheet对象
		self.opera_excel.load_workbook(self.data.dataFilePath)
		self.opera_excel.get_sheet_by_name(self.data.sheetName)



	#去获取excel行数,就是我们的case个数	
	def get_case_lines(self):
		try:
			case_lines = self.opera_excel.get_row_number()
			return case_lines
		except Exception as e:
			raise e

	#获取是否执行
	def get_is_run(self, row):
		flag = None
		run_model = self.opera_excel.get_cell_value(row, self.data.run)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	#是否携带header
	def is_header(self,row):

		header = self.opera_excel.get_cell_value(row,self.data.header)
		if header != '':
			return header
		else:
			return None

	#获取请求方式
	def get_request_method(self,row):
		try:
			request_method = self.opera_excel.get_cell_value(row,self.data.request_way)
			return request_method
		except Exception as e:
			raise e

	#获取url
	def get_request_url(self,row):
		try:
			url = self.opera_excel.get_cell_value(row,self.data.url)
			return url
		except Exception as e:
			raise e

	#获取请求数据
	def get_request_data(self,row):
		data = self.opera_excel.get_cell_value(row,self.data.data)
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
		expect = self.opera_excel.get_cell_value(row,self.data.expect)
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
		self.opera_excel.write_cell(value,row,colsnum)

	#获取依赖数据的key
	def get_depend_key(self,row):

		depent_key = self.opera_excel.get_cell_value(row,8)
		if depent_key == "":
			return None
		else:
			return depent_key

	#判断是否有case依赖
	def is_depend(self,row):

		depend_case_id = self.opera_excel.get_cell_value(row,7)
		if depend_case_id == "":
			return None
		else:
			return depend_case_id

	#获取数据依赖字段
	def get_depend_field(self,row):
		data = self.opera_excel.get_cell_value(row,9)
		if data == "":
			return None
		else:
			return data

	# 根据case_id获取整行内容
	def id_get_row_data(self, id):
		try:
			row_num = self.id_get_row_num(id)
			row_data = self.opera_excel.get_row_data(row_num)
			return row_data
		except Exception as e:
			raise e

	# 根据case_id获取行号
	def id_get_row_num(self, id):
		row_num = 1
		cols_data = self.opera_excel.get_column_data("A")
		for col_data in cols_data:
			if id == col_data.value:
				return row_num
			row_num = row_num + 1

