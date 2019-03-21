from src.main.python.utils.ReadConfig import ReadConfig
from src.main.python.utils.ProcessNameList import ProcessNameList
import os


class OpenBatch:
    # 公共属性
    process_name_list = ProcessNameList()
    # 私有属性
    _open_files = []

    # 构造函数
    def __init__(self):
        pass

    def open_batch_file(self, config_file_path):
        config = ReadConfig(config_file_path)
        names = config.get_will_open_process_names()
        for name in names:
            running = self.process_name_list.process_is_running(name)
            # running是个boolean类型，not false 即 true
            if not running:
                # 执行对应的程序
                process_path_by_name = config.get_will_open_process_path_by_name(name)
                print('%s is not running, path is %s' % (name, process_path_by_name))
                os.system(process_path_by_name)
            else:
                print('%s is running' % name)


if __name__ == '__main__':
    batch = OpenBatch()
    batch.open_batch_file('../config/processes.properties')

