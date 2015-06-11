# encoding:utf-8
import os
import sys

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


print common_args

print extra_link_args
print compile_args
extensions = [
    # Extension(name="ltsapi.MdApi",
    #           sources=["ltsapi/MdApi.pyx"],
    #           extra_compile_args=compile_args,
    #           extra_objects=["securitymduserapi.lib"] if sys.platform == "win32" else None,
    #           extra_link_args=extra_link_args,
    #           libraries=["securitymduserapi"],
    #           **common_args),

    # Extension(name="ltsapi.Trader",
    #           sources=["ltsapi/Trader.pyx"],
    #           extra_objects=["securitytraderapi.lib"] if sys.platform == "win32" else None,
    #           extra_compile_args=compile_args,
    #           extra_link_args=extra_link_args,
    #           libraries=["securitytraderapi"],
    #           **common_args)
    Extension(name="ltsapi.MdApi",
              sources=["ltsapi/MdApi.pyx"],
              extra_compile_args=compile_args,
                            extra_objects=[os.path.join(lts_dir, "securitymduserapi.so")],

              # extra_objects=["securitymduserapi.so"] ,
              extra_link_args=extra_link_args,
             # libraries=["securitymduserapi"],
              **common_args),
]

setup(
    name='python LTS Api',
    version="1.0.0",
    author="xiaomomi",
    author_email="365504029@qq.com",
    description="This is LTS stock Interface python wrapper",
    include_package_data=True,
    install_requires=["Cython>=0.22"],
    setup_requires=["Cython>=0.22"],
    packages=find_packages(),
    package_data={"": package_data},
    cmdclass={"build_ext": build_ext},
    ext_modules=(extensions),
    exclude_package_data={"": ["*.cpp"]},
    platforms=["windows", "linux"]

)
