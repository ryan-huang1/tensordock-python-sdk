from setuptools import setup, find_packages

setup(
    name="tensordock",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Ryan Huang",
    author_email="ryan@stdint.com",
    description="A Python SDK for TensorDock API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tensordock-python-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)