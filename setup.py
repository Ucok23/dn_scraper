from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="dn_scraper",
    version="0.0.1",
    author="Ucok Isa Lubis",
    author_email="ulubis98@gmail.com",
    description="A simple web scraper for detik.com news.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["beautifulsoup4", "requests"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
