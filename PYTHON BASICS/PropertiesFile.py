# -*- coding: utf-8 -*-
# @File    : PropertiesFile.py
# @Time    : 4/29/2021 4:48 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

from configparser import ConfigParser
config = ConfigParser()
config.read("C:\\Users\\mkandukx\\PycharmProjects\\PyTestSample\\PYTHON BASICS\\config.properties")
cfg = config.sections()
print(cfg)

cfg1 = config['Section_Name']['Name1']
print(cfg1)

cfg2 = config['Section_Env']['Env3']
print(cfg2)

details_dict = config.items('Section_Name')
print(dict(details_dict))

