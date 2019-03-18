class ReadConfig:
    def __init__(self):
        pass

    def read_config_from_file(self):
        import configparser

        cf = configparser.ConfigParser()
        cf.read('../config/processes.properties')

        # 配置文件中所有的配置头
        names = cf.sections()
        print(names)

        # 获得对应头 '[idea.exe]'下的'path'配置项
        get = cf.get('idea.exe', 'path')
        print(get)


if __name__ == '__main__':
    config = ReadConfig()
    config.read_config_from_file()
