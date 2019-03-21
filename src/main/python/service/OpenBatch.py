from src.main.python.utils.ReadConfig import ReadConfig
from src.main.python.utils.ProcessNameList import ProcessNameList
import os
import logging

logging.basicConfig(level=logging.DEBUG)


class OpenBatch:
    # 公共属性
    __process_name_list = ProcessNameList()
    # 私有属性
    __cmd = 'start \"\" \"%s\"&ping localhost -n %d'

    # 构造函数
    def __init__(self):
        pass

    def open_batch_file(self, config_file_path):
        config = ReadConfig(config_file_path)
        names = config.get_will_open_process_names()
        i = 1
        for name in names:
            running = self.__process_name_list.process_is_running(name)
            # running是个boolean类型，not false 即 true
            if not running:
                # 执行对应的程序
                process_path_by_name = config.get_will_open_process_path_by_name(name)
                logging.debug('%s is not running,will start, path is %s' % (name, process_path_by_name))
                # ++i只是正正得正数而已，不是i = i + 1
                i = i + 1
                os.system(self.__cmd % (process_path_by_name, i))
            else:
                logging.debug('%s is running' % name)

    def testOsSystem(self):
        os.system(self.__cmd % ('E:/MySoftware/MobaXterm/MobaXterm.exe', 1))


if __name__ == '__main__':
    batch = OpenBatch()
    batch.open_batch_file('../config/processes.properties')
    # batch.testOsSystem()
