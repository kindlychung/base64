
from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool
from pathlib import Path
import os
import shutil


class base64Conan(ConanFile):
    name = "base64"
    version = "1.0.2"
    license = "zlib"
    author = "René Nyffenegger"
    url = "https://github.com/kindlychung/base64"
    description = "Base64 encoding and decoding library. This is slightly modified based on Rene's original work."
    topics = ("cpp", )
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    requires = ()
    generators = "cmake"
    exports_sources = "src/%s/*" % name, "src/CMakeLists.txt", "src/*.cmake"

    def system_requirements(self):
        pack_list = None
        if os_info.linux_distro == "ubuntu":
            pack_list = []
        if pack_list:
            for p in pack_list:
                installer = SystemPackageTool()
                installer.install(p)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("base64/*.hpp", dst="include", src="src")
        self.copy("base64/*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def imports(self):
        self.copy("*", dst="include", src="include")
        self.copy("*", dst="bin", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["base64"]
