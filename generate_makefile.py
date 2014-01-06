#!/usr/bin/env python

# Copyright (C) 2013 Cybojenix <anthonydking@slimroms.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from re import sub

vendor = "lge"
device = "e400"

with open(device + "-vendor-blobs.mk", "w") as blobs:
    blobs.write("# Copyright (C) 2011 The CyanogenMod Project\n\
#\n\
# Licensed under the Apache License, Version 2.0 (the \"License\");\n\
# you may not use this file except in compliance with the License.\n\
# You may obtain a copy of the License at\n\
#\n\
#      http://www.apache.org/licenses/LICENSE-2.0\n\
#\n\
# Unless required by applicable law or agreed to in writing, software\n\
# distributed under the License is distributed on an \"AS IS\" BASIS,\n\
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n\
# See the License for the specific language governing permissions and\n\
# limitations under the License.)\n\
\n\
# This file was generated with generate_makefile.py\n\
\n\
PRODUCT_COPY_FILES += \\\n")
    for dirname, dirnames, filenames in os.walk('proprietary'):

        for filename in filenames:
            path = os.path.join(dirname, filename)
            inpath = "/".join(["vendor", vendor, device, path])
            inpath = "".join(["\t", inpath])
            outpath = sub("^proprietary/", "system/", path)
            outpath = " ".join([outpath, "\\\n"])
            blobs.write(":".join([inpath, outpath]))
    blobs.seek(-3, os.SEEK_END)
    blobs.truncate()
