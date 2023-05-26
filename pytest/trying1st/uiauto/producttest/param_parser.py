import json
import configparser
import yaml
from configparser import ConfigParser
# 项目中必须设定绝对路径作为基准rootdir，不能全部采用相对路径！！！


conf = '..\\..\\cfg\\projcfg.ini'
# yamlf = '.\\data\\bookmsg.yml'


def conf_parser(conf):
    Config = ConfigParser()
    Config.read(conf, encoding='utf-8')
    sections = Config.sections()
    # print(sections)
    cfgmsg = []
    for key in sections:
        cfgmsg += Config.items(key)
        # print(Config.items(key))
        # print(dict(Config.items(key)))
    return dict(cfgmsg)


yamlf = conf_parser(conf)
# yamlf = conf_parser(conf)['ui_product_data']


def yaml_parser(yamlf):
    with open(yamlf, 'r', encoding='utf-8') as fstream:
        msg = yaml.safe_load_all(fstream)
        info = list(msg)
    print(info)
    return info


# yaml_parser(yamlf)
# print(conf_parser(conf))
