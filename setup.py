#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="esbulkstream",
    version="0.0.1",
    author="Josh Bressers",
    author_email="josh@bress.net",
    description="Elasticsearch Bulk Streamer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshbressers/es-bulk-stream",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=[
        'elasticsearch'
    ],
    setup_requires=['pytest-runner', 'Elasticsearch'],
    tests_require=['pytest']
)

