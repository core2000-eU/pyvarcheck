#Copyright (c) 2026 Benjamin Winter
#This file is part of pyvarcheck which is released under the MIT License.
#See file LICENSE or go to https://github.com/core2000-eU/pyvarcheck for full license details.

#DESCRIPTION
#Easy, high-level var testing for python with auto-conversion features.

import                          setuptools
from pathlib import             Path

parent_dir = Path(__file__).parent
long_description = (parent_dir / "README.md").read_text(encoding="utf-8")

setuptools.setup (
    name =                      "pyvarcheck", 
    version =                   '0.0.1',
    author =                    "Benjamin Winter",
    license=                    "MIT",
    description =               "Easy, high-level var testing for python with auto-conversion features",
    long_description =                  long_description,
    long_description_content_type =     "text/markdown",
    keywords =                  ['python', 'var', 'arg', 'check', 'convert'],
    classifiers =               [
                                    "Development Status :: 4 - Beta",
                                    "Programming Language :: Python :: 3",
                                    "Operating System :: OS Independent"
                                ],
    packages =                  setuptools.find_namespace_packages(where="src/P"),
    package_dir =               {"": "src/P"},
    install_requires =          [],
    package_data =              {},
)
