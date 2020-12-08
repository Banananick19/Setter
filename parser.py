import re

class ParserConfig:

    def __init__(self, file=str('configs.txt')):
        with open(file) as f:
            self.text = f.read()
        self.parse(self.text, rtn=False)

    def parse(self, text, rtn=True):
        result = dict()
        config_names_pattern = re.compile('\[config (.*)\]')
        for name in re.finditer(config_names_pattern, self.text):
            result[name] = re.search('\[config {}\](.*)\[endconfig\]'.format(name), self.text).group()
        #TODO: need parse match from re.search for list of paths
        if rtn:
            return result
        else:
            self.result = result

