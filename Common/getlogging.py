import logging
import os
import time
from Common import dir_config

class GetLogging(object):
        '''定义log,(‘DEBUG’、‘INFO’、‘WARNING’、‘ERROR’、‘CRITICAL’)'''
    
        def __init__(self):
            self.nowtime = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())  #error:文件名不能存在空格
            self.log_name = self.nowtime + '-'+'log.txt'
            self.log_path = os.path.join(dir_config.logs_dir,self.log_name)
            
        # logging.basicConfig
        def get_logging(self,level,msg):
            getlogs = logging.getLogger()
            getlogs.setLevel("DEBUG") #定义抓取log的级别
            #配置log格式
            formatter = logging.Formatter("%(asctime)s %(name)s %(filename)s %(module)s %(funcName)s (line:%(lineno)d):[%(levelname)s] %(message)s")
            #创建输出渠道
            ch = logging.StreamHandler() #输出到控制台---->控制是否输出到html测试报告中
            ch.setLevel("INFO") #设置输出的级别
            ch.setFormatter(formatter)
            fh = logging.FileHandler(self.log_path,encoding="utf-8") #输出到文件
            fh.setLevel("INFO") #设置输出的级别
            fh.setFormatter(formatter)
            #日志收集器与输出渠道对接
            getlogs.addHandler(ch)
            getlogs.addHandler(fh)
            if level == "DEBUG":
                #日志输出
                getlogs.debug(msg)
            elif level =="INFO":
                getlogs.info(msg)
            elif level == "WARNING":
                getlogs.warning(msg)
            elif level == "ERROR":
                getlogs.error(msg)
            else:
                getlogs.critical(msg)
        
            #渠道需要移除
            getlogs.removeHandler(ch)
            getlogs.removeHandler(fh)


    




if __name__ == "__main__":
    getlogging = GetLogging()
    print(type(getlogging.log_path))
    print(getlogging.nowtime)
    getlogging.get_logging("ERROR","hehehehe")
    # print(dir_config.base_dir)