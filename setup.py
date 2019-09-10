import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-renderservice",
    version="0.0.1",
    author="Hannes Lohmander",
    author_email="hannes@aldowntown.com",
    description="A package to use a renderservice to render parts of a Django template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aldowntown/django-renderservice",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)