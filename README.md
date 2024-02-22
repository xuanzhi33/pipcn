# pipcn

快速、方便的使用pip的国内镜像源安装/更新包~
默认使用清华大学pip镜像：https://pypi.tuna.tsinghua.edu.cn/simple

[![PyPI - Version](https://img.shields.io/pypi/v/pipcn.svg)](https://pypi.org/project/pipcn)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pipcn.svg)](https://pypi.org/project/pipcn)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install pipcn
```

## Usage

```console
pipcn <package>
```
以上命令相当于：
```console
pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple <package>
```

## License

`pipcn` is distributed under the terms of the [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html) license.
