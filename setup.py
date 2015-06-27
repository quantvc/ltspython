# encoding:utf-8
import os
import sys
from distutils.core import Extension

from setuptools import setup, find_packages

project_dir = os.path.join(os.path.dirname(__file__), "ltsapi")

lts_dir = os.path.abspath(os.path.join(project_dir, "LtsApi"))

compile_args = []
extra_link_args = []
package_data = ["LtsApi/*.xml"]

if sys.platform == "linux":
    compile_args = ["-O3", "-Wall"]
    extra_link_args = ['-g']
    package_data.append("LtsApi/*.so")
elif sys.platform == "win32":
    compile_args = ["/GR", "/EHsc"]
    extra_link_args = []
    package_data.append("LtsApi/*.dll")

common_args = {
    "include_dirs": [lts_dir],
    "library_dirs": [lts_dir],
    "language": "c++",
}

extensions = [

    Extension(name="ltsapi.md_api",
              sources=["ltsapi/md_api.cpp","ltsapi/md_wrapper.cpp","lts/api_struct.cpp"],
              extra_compile_args=compile_args,
              extra_link_args=extra_link_args,
              libraries=["securitymduserapi"],
              **common_args),
]

setup(
    name='python LTS Api',
    version="1.0.0",
    author="winton.wang",
    author_email="winton@quant.vc",
    description="This is LTS stock Interface python wrapper",
    include_package_data=True,
    packages=find_packages(),
    package_data={"": package_data},
    ext_modules=extensions,
    exclude_package_data={"": ["*.cpp"]},
    platforms=["windows", "linux"]

)
