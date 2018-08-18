from configparser import ConfigParser

from Iconfigreader import IConfigReader

class DBConfigReader(IConfigReader):
    def __init__(self, config):
        super().__init__(config)

    def get_value(self, key):
        cfg = ConfigParser()
        
        cfg.read(self.config_file)
        for item in cfg.items():
            print(item)
        print(cfg['DEFAULT']['name'])

if __name__ == '__main__':
    c = DBConfigReader('../config/db.cfg')
    c.get_value('1')