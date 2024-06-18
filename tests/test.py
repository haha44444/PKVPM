import os
from pkvpm.parser import Parser

import yaml

parser = Parser()

# 示例使用，读取测试需要的一共3个文件（test.yml, test.json, test.pkv）
# An example of using the test requires a total of 3 files (test.yml, test.json, test.pkv)
test_yml_path = os.path.join(os.path.dirname(__file__), 'test.yml')
test_json_path = os.path.join(os.path.dirname(__file__), 'test.json')
test_pkv_path = os.path.join(os.path.dirname(__file__), 'test.pkv')


# 读取PKV文件/Read PKV file
with open(r"./test2.pkv", 'r', encoding='utf-8') as file:
    test_pkvpm_content = file.read()
# 将PKVPM格式数据转换为YAML格式/Convert PKVPM format data to YAML format
pkvpm_to_yaml_content = parser.to_yaml(test_pkvpm_content, test_yml_path)
print(f"PKVPM to YAML:\n{pkvpm_to_yaml_content}")



# # 读取YAML文件/Read YAML file
# with open(r"./test.yml", 'r', encoding='utf-8') as file:
#     test_yml_content = file.read()
# # 将YAML数据转换为PKVPM格式
# yaml_to_pkvpm_content = parser.parse(test_yml_content)
# print(f"YAML to PKVPM:\n{yaml_to_pkvpm_content}")

# class MultiLineStr(str): pass
#
# def literal_presenter(dumper, data):
#     return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
#
# yaml.add_representer(MultiLineStr, literal_presenter)
#
# data = {
#   'literal': MultiLineStr("""这是一个多行
# 字符串，将会保留
# 换行符。""")
# }
#
# yaml_str = yaml.dump(data, allow_unicode=True)
# print('\n' + yaml_str)


