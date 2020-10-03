import setuptools


with open("README.md") as f:
    long_description = f.read()

requirements = [
    "tortoise-orm>=0.16.14",
    "pypika-gis>=1.3.0",
    "shapely>=1.7.1",
    "geojson>=2.5.0",
]

setuptools.setup(
    name="tortoise-gis",
    version="0.1.2",
    author="Eduardo Ribeiro Rezende",
    author_email="eduardorbr7@gmail.com",
    license="MIT",
    description="Geometrical and Geographical support for Tortoise ORM.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/revensky/tortoise-gis",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=requirements,
    keywords=["Tortoise", "GIS"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
