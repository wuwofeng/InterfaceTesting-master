import json
import os
from util.opreate_login import Login
#当前路径
curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
#根路径
rootPath = os.path.abspath(os.path.dirname(curPath))
print(rootPath)

#操作的json文件的路径
class UpdateJson(object):
    def __init__(self, file_oldname=None, file_newname =None ):
        if file_oldname:
            self.file_oldname = file_oldname
            self.file_newname = file_newname
        else:
            #配置使用的json文件名称和路径,可以配置新的文件或者旧的文件地址
            self.file_oldname = r"data/TestcaseHeaders3.json"
            self.file_oldname = os.path.join(rootPath, self.file_oldname)
            self.file_newname = r"data/TestcaseHeaders3.json"
            self.file_newname = os.path.join(rootPath, self.file_newname)
            #print("self.file_name: ", self.file_oldname)

        self.data = self.update_json()

    def update_json(self):
        #更新登陆获取的token、sign和sessionId
        with open(self.file_oldname,'r',encoding='utf-8') as fp:
            data =json.load(fp)
            data['token']= Login().login()[0]
            data['sessionId'] = Login().login()[1]
            data['sign'] = Login().login()[2]
        #最终可以在新文件上修改，也可以在借文件中修改
        with open(self.file_oldname,'w',encoding='utf-8') as fp2:
            json.dump(data, fp2)
            return data

if __name__ == '__main__':
    oj = UpdateJson("../data/TestcaseHeaders3.json")
    # print(oj.update_json())
    # print(type(oj))
    # print(oj.data)