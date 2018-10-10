import configparser
from data import data_config

class ParseCofigFile():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(data_config.confFilePath)

    # 读取配置文件
    def getItemsSection(self, sectionName):
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self, sectionName, optionName):
        value = self.cf.get(sectionName, optionName)
        return value