"""
operation_data.py
读写文件  csv/Excel表格
使用pandas
"""
import pandas
import os

# 读取csv文件
# csv = pandas.read_csv(r"E:\0927软件测试精英班\13_web自动化项目\20191213web自动化项目day_1\code\ECShop\data\login_data.csv")
# # print(csv)
# # print(csv.index.values)  # csv文件行索引
# # print(csv.loc[0])
# print(csv.values.tolist())  # 读取的数据为列表嵌套列表格式 [[],[],[]]
# # 读取数据为列表嵌套字典:[{},{}]
# # data = []  # 创建空列表,盛放数据
# # for i in csv.index.values:  # 遍历行
# #     row_data = csv.loc[i].to_dict()  # 逐行取出数据并且转换为字典格式
# #     data.append(row_data)
# data = [csv.loc[i].to_dict() for i in csv.index.values]  # 将csv文件读取成列嵌套字典
# print(data)

"""读取Excel文件"""
# 读取表格
# excel = pandas.read_excel(r"E:\0927软件测试精英班\13_web自动化项目\20191213web自动化项目day_1\code\ECShop\data\userdata.xls")
# data_list = excel.values.tolist()  # 读取的数据为列表嵌套列表格式 [[],[],[]]
# print(data_list)
# data_dict = [excel.loc[i].to_dict() for i in excel.index.values]  # 将csv文件读取成列嵌套字典
# print(data_dict)

class OperationFlie:
    def __init__(self,filename:str):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\data"  # 相当于"../data"
        self.filepath = os.path.join(base_path,filename)  # 文件路径
        if filename.split(".")[-1] == "csv":
            self.file = pandas.read_csv(self.filepath)  # 读取csv格式的文件
        else:
            self.file = pandas.read_excel(self.filepath)

    def get_data_to_list(self):
        """
        将数据读取成列表嵌套列表格式
        :return:
        """
        return self.file.values.tolist()

    def get_data_to_dict(self):
        """
        将数据读取成列表嵌套字典格式
        :return:
        """
        return [self.file.loc[i].to_dict() for i in self.file.index.values]

    def write_data_to_excel(self,data:list):
        """
        更新表格
        1.读取表格元数据
        2.将新数据插入在第一行位置
        3.将源数据追加在第一行之后
        """
        # 读取源数据
        old_data = self.get_data_to_list()  #[[],[],[]]
        # 添加新数据在第一行
        self.file.loc[0] = data  # 指定插入行行号
        # 将老数据追在在第一行之后
        for i in range(1,len(old_data)+1):
            self.file.loc[i] = old_data[i-1]
        self.file.to_excel(self.filepath,index=None)  # 保存数据



if __name__ == '__main__':
    filename = "register_data.xls"
    data = ["Tom","Tom@qq.com","test123456","13800138000"]
    OperationFlie(filename).write_data_to_excel(data)