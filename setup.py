import setuptools

version = "0.0.0"
long_description = "Utility library to help resting for regularity and clusters"

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read()

setuptools.setup(
    name="snakeden",
    version=version,
    author="Daniel Kirkegaard Mouritsen",
    author_email="daniel.mouritsen@gmail.com",
    description="Library for cluster analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/justdanyul/snakeden",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "scikit-learn",
        "scipy",
    ],
    python_requires=">=3.7",
)
