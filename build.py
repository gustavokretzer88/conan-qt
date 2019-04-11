#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_default
import os

if __name__ == "__main__":

    builder = build_template_default.get_builder(build_policy="missing")
    if os.getenv("CONAN_DOCKER_IMAGE", "").startswith("conanio/android-clang8"):
        for it in builder.items:
            it.settings["os"] = "Android"
            it.settings["arch"] = os.getenv("CONAN_ARCHS")
            it.settings["compiler"] = "clang"
            it.settings["compiler.version"] = "8"
            it.settings["compiler.libcxx"] = "libc++"
    builder.run()
