import yaml
import os

# path = os.path.join(os.path.realpath(os.path.dirname(__file__)),'config.yaml')
# print(os.path.dirname(__file__))
# print(path)
# with open(path,'r',encoding='utf-8') as f:
#     file_data = f.read()
#     datas = yaml.load_all(file_data)
#     print(datas[0])
#     for data in datas:
#         print(data)

class GetYaml(object):


    def __init__(self):
        self.datapath = os.path.join(os.path.realpath(os.path.dirname(__file__)),'config.yaml')
    
    def load_all_yaml(self):
        with open(self.datapath,'r',encoding='utf-8') as f:
            datas = yaml.load_all(f.read())
            return datas

getyaml = GetYaml()
testdata = getyaml.load_all_yaml()
for data in testdata:
    print(data)