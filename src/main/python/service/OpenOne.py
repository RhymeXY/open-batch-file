class OpenOne:
    # 公共属性
    from src.main.python.utils.ProcessNameList import ProcessNameList
    process_name_list = ProcessNameList()
    # 私有属性
    _open_files = []
    # 构造函数
    def __init__(self):
        pass

    def main(self):
        self.open_one_file()



    def open_one_file(self):
        import os
        # 使用os.system()函数打开记事本程序
        self.process_name_list.process_is_running()
        os.system('notepad')


if __name__ == '__main__':

    one.read_config_from_py_file()

    # from src.main.python.utils.ProcessNameList import ProcessNameList
    # name_list = ProcessNameList()
    # list_main = name_list.main()
    # print(list_main)
    # print(name_list.process_is_running('System'))