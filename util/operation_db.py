import pymysql
from util.operation_conf import ParseCofigFile


class OperationDataBase:

    def __init__(self):
        self.parseCF = ParseCofigFile()
        self.database_host = self.parseCF.getOptionValue(sectionName="database", optionName="host")
        self.database_user = self.parseCF.getOptionValue(sectionName="database", optionName="username")
        self.database_pwd = self.parseCF.getOptionValue(sectionName="database", optionName="password")
        self.database_type = self.parseCF.getOptionValue(sectionName="database", optionName="type")

    # 连接数据库并获得游标对象
    def connect_db(self):
        try:
            self.db = pymysql.connect(self.database_host, self.database_user, self.database_pwd, self.database_type)
            self.cursor = self.db.cursor()
            return self.cursor
        except Exception as e:
            raise e

    # 使用 execute()  方法执行 SQL
    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
        except:
            self.db.rollback()

    # 获取SQL执行结果
    def get_result(self):
        try:
            self.results = self.cursor.fetchall()
            return self.results
        except Exception as e:
            raise e

    # 提交到数据库
    def commit(self):
        try:
            self.db.commit()
        except Exception as e:
            raise e

    # 关闭数据库
    def close_db(self):
        try:
            self.db.close()
        except Exception as e:
            raise e


sql = "SELECT * FROM kisso.account WHERE account = 15666666661"

if __name__ == '__main__':
    op = OperationDataBase()
    op.connect_db()
    op.execute_sql(sql)
    op.get_result()
    op.close_db()
