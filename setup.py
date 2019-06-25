
import setuptools

__version__ = '0.0.1'

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="scooby",
    version=__version__,
    author="Dieter Werthmuller & Bane Sullivan",
    author_email="info@pyvista.org",
    description="A Great Dane turned Python environment detective",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/banesullivan/scooby",
    install_requires=['psutil',]
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
    ),
)
