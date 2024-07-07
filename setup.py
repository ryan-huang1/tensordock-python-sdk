from setuptools import setup, find_packages

setup(
    name="tensordock",
    version="0.1.1",  # Incremented the version number
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Ryan Huang",
    author_email="ryan@stdint.com",
    description="A Python SDK for TensorDock API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ryan-huang1/tensordock-python-sdk",
    project_urls={
        "Bug Tracker": "https://github.com/ryan-huang1/tensordock-python-sdk/issues",
        "Documentation": "https://github.com/ryan-huang1/tensordock-python-sdk/blob/main/DOCS.md",
        "Source Code": "https://github.com/ryan-huang1/tensordock-python-sdk",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)