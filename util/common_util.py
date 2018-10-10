import operator


class CommonUtil:

    @staticmethod
    # 判断两个字符串是否相等
    def is_contain(str_one, str_two):
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    @staticmethod
    # 判断一个字典是否在另一个字典
    def is_equal_dict(dict_one, dict_two):
        dict1 = dict_one.replace(" ", "").replace("\n", "")
        dict2 = dict_two.replace(" ", "").replace("\n", "")
        is_requal = operator.eq(dict1, dict2)
        return is_requal
