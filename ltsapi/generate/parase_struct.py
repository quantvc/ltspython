# -*- coding=utf-8 -*-


"""
生成结构化的代码
"""

import re
import os
from collections import OrderedDict

class Parse(object):
    """
    解析结构体
    """

    def __init__(self, type_file, struct_file):

        self.type_header_file = type_file

        self.struct_header_file = struct_file

        self.data_type = OrderedDict()
        self.struct = OrderedDict()

    def parse_datatype(self):
        """
        处理 UserApiDataType file.
        """
        for line in open(self.type_header_file):
            if line.startswith("typedef"):
                result = re.findall("\w+", line)
                name = result[2]
                type_ = result[1]

                if len(result) == 4 and type_ == "char":
                    self.data_type[name] = {
                        "type": "str",
                        "length": int(result[3])
                    }
                elif type_ == "char":
                    self.data_type[name] = {
                        "type": "str",
                    }
                else:
                    self.data_type[name] = {
                        "type": type_,
                    }
        return self.data_type

    def parse_struct(self):
        """
        解析结构体定义
        """
        self.parse_datatype()

        for line in open(self.struct_header_file):
            if line.startswith("struct"):
                name = line.strip().split()[1]
                self.struct[name] = OrderedDict()

            if line.strip().startswith("TSecurity"):
                field_type = line.strip().split()[0]
                field_name = line.strip().split()[1][:-1]
                self.struct[name][field_name] = self.data_type[field_type]

        return self.struct


def generate_struct(struct, py_file):
    for item in struct:

        py_file.write("class %s(Base):\n" % item)
        py_file.write("    def __init__(self,%s):\n" % ",".join([field for field in struct[item]]))

        for field in struct[item]:
            if struct[item][field]["type"] == "double":
                py_file.write("        self.%s=float(%s)\n" % (field, field))
            if struct[item][field]["type"] == "int" or struct[item][field]["type"] == "short":
                py_file.write("        self.%s=int(%s)\n" % (field, field))
            if struct[item][field]["type"] == "str":
                py_file.write("        self.%s=%s\n" % (field, field))


def generate_interface():
    lts_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    type_file = os.path.join(lts_path, "LtsApi/SecurityFtdcUserApiDataType.h")
    struct_file = os.path.join(lts_path, "LtsApi/SecurityFtdcUserApiStruct.h")

    parse = Parse(type_file, struct_file)
    struct = parse.parse_struct()

    # generate python
    py_file = file("UserApiStruct.py", "w")
    py_file.write('#-*- coding=utf-8 -*-\n"""' + __doc__ + '"""\n')

    generate_struct(struct, py_file)

    for item in struct:
        py_file.write("%s=%s\n" % (item[13:-5], item))

    py_file.close()


if __name__ == "__main__":
    generate_interface()
