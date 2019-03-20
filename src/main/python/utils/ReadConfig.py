import configparser


class ReadConfig:

    # 读取配置文件的类
    __cf = configparser.ConfigParser()
    __config_file_path = str()

    def __init__(self, config_file_path):
        self.__config_file_path = config_file_path
        self.__read_config_from_file()

    # 读取配置文件到__cf
    def __read_config_from_file(self):
        self.__cf.read(self.__config_file_path, encoding='UTF-8')

    # 配置文件中所有的配置头
    def get_will_open_process_names(self):
        names = self.__cf.sections()
        # print(names)
        return names

    # 获得对应头下的'path'配置项
    def get_will_open_process_path_by_name(self, name):
        path = self.__cf.get(name, 'path')
        # print(get)
        return path


if __name__ == '__main__':
    config = ReadConfig()
    config.get_will_open_process_names()
    config.get_will_open_process_path_by_name('chrome.exe')
