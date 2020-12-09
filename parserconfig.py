import configparser

def get_configs(file_path):
    parser = configparser.ConfigParser()
    parser.read_file(open(file_path, encoding='utf-8'))
    return parser
