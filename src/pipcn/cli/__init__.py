# SPDX-FileCopyrightText: 2024-present xuanzhi33 <xuanzhi33@qq.com>
#
# SPDX-License-Identifier: GPL-3.0-only

from pipcn.__about__ import __version__
import sys
import subprocess
HELP = """
pipcn: 快速、方便的使用pip的国内镜像源安装/更新包~

by xuanzhi33

用法：
pipcn <package>
以上命令等价于：
pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple <package>

Usage:
pipcn <package>
The above command is equivalent to:
pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple <package>
"""

MIRROR = "https://pypi.tuna.tsinghua.edu.cn/simple"
PYTHON_PATH = sys.executable
def pipcn():
    argv = sys.argv
    if len(argv) != 2:
        print(HELP)
        return
    
    package = argv[1]
    if package == "-v" or package == "--version":
        print(f"pipcn version {__version__}")
        return

    if package == "-h" or package == "--help":
        print(HELP)
        return
    
    print(f"pipcn: Installing/Updating {package} from {MIRROR}...")
    commands = [PYTHON_PATH, "-m", "pip", "install", "--upgrade", "-i", MIRROR, package]
    print(f"Running command: {' '.join(commands)}")
    subprocess.run(commands)
