# -*- coding=utf-8 -*-

import os

from ltsapi.generate.parase_struct import Parse


def generate_hpp():
    """
    生成头文件 struct.h 结构
    """
    lts_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    type_file = os.path.join(lts_path, "LtsApi/SecurityFtdcUserApiDataType.h")
    struct_file = os.path.join(lts_path, "LtsApi/SecurityFtdcUserApiStruct.h")

    parse = Parse(type_file, struct_file)
    struct = parse.parse_struct()

    struct_header_file = file("trader_struct.h", "w")

    for item in struct:
        struct_header_file.write("PyObject * new_%s(%s * p);\n" % (item, item))
        struct_header_file.write("%s * from_%s(PyObject * p);\n" % (item, item))

    struct_header_file.close()


def struct_type(type_, length):
    """
    """

    if type_ == "str" and length:
        return "s"
    elif type_ == "str" and length is None:
        return "c"
    elif type_ == "double":
        return "d"
    elif type_ == "short":
        return "h"
    elif type_ == "int":
        return "i"


def generate_cpp():
    lts_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    type_file = os.path.join(lts_path, "LtsApi/SecurityFtdcUserApiDataType.h")
    struct_file = os.path.join(lts_path, "LtsApi/SecurityFtdcUserApiStruct.h")

    parse = Parse(type_file, struct_file)
    struct = parse.parse_struct()

    struct_cpp_file = file("struct.cpp","w")

    for item in struct:
        struct_cpp_file.write("PyObject * new_%s(%s * p){\n" % (item, item))
        struct_cpp_file.write("""   if(p==NULL){
                                    Py_INCREF(Py_None);
                                return Py_None;\n
                                }
                              """)
        type_def = "".join(
            [struct_type(struct[item][field]["type"], struct[item][field].get("length", None)) for field in
             struct[item]])
        struct_cpp_file.write('return PyObject_CallMethod(mod,(char *)"%s",(char*)"%s",\n ' % (item, type_def))
        struct_cpp_file.write(', '.join(['p->%s' % field for field in struct[item]]))
        struct_cpp_file.write(");\n}\n")

        struct_cpp_file.write("%s * from_%s(PyObject *p){\n " % (item, item))
        struct_cpp_file.write("    %s *t = (%s *)calloc(1,sizeof(%s));\n" % (item, item, item))
        struct_cpp_file.write("    memset(t,0,sizeof(%s));\n" % (item))
        for field in struct[item]:

            type_ = struct[item][field]["type"]
            length = struct[item][field].get("length", None)
            if type_ == "str" and length:
                struct_cpp_file.write(
                    ' strcpy( t->%s, PyString_AsString(PyObject_GetAttrString(p,"%s")));\n' % (field, field))

            elif type_ == "str" and length is None:
                struct_cpp_file.write("   t->%s =" % field)
                struct_cpp_file.write('   PyString_AsString(PyObject_GetAttrString(p,"%s"))[0];\n' % field)
            elif type_ == "double":
                struct_cpp_file.write("  t->%s =" % field)
                struct_cpp_file.write('  PyFloat_AsDouble(PyObject_GetAttrString(p,"%s"));\n' % field)
            elif type_ == "int":
                struct_cpp_file.write("  t->%s =" % field)
                struct_cpp_file.write('  PyInt_AsLong(PyObject_GetAttrString(p,"%s"));\n' % field)
            elif type_ == "short":
                struct_cpp_file.write("  t->%s =" % field)
                struct_cpp_file.write(' PyInt_AsLong(PyObject_GetAttrString(p,"%s"));\n' % field)
            else:
                print "unknown type", type_

        struct_cpp_file.write("\n  return t;\n};\n")

    struct_cpp_file.close()

if __name__ == "__main__":
    generate_cpp()