import re

from setuptools import setup, find_packages

def get_version():
    with open("apollo_modules/__init__.py") as f:
        return re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="apollo_modules",  # Replace with your project name
    version=get_version(),  # Initial version
    author="MingfeiCheng",
    author_email="snowbirds.mf@gmail.com",
    description="This is a package including baidu apollo' proto modules",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MingfeiCheng/ApolloPyProto",  # URL to your project
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Use your license here
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the Python version compatibility
    install_requires=[
        # Add dependencies here, e.g., 'requests', 'numpy'
        'protobuf==3.20.1'
    ],
)
