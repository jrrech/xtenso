import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="xtenso",
    version="0.0.1",
    url="",
    license="BSD",
    maintainer="Jonatas Rech",
    maintainer_email="jonatas.rech@gmail.com",
    description="Translates a number given in numerals to it's spelled-out form",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest"]},
)
