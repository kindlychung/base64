
from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool
from pathlib import Path
import os
import shutil

class base64TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*", dst="include", src="include")
        self.copy("*", dst="bin", src="lib")

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%sexample" % os.sep)
