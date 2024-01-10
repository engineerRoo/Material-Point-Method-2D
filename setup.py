"""Python setup.py for material_point_method_2d package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("material_point_method_2d", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="material_point_method_2d",
    version=read("material_point_method_2d", "VERSION"),
    description="Awesome material_point_method_2d created by engineerRoo",
    url="https://github.com/engineerRoo/Material-Point-Method-2D/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="engineerRoo",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["material_point_method_2d = material_point_method_2d.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
