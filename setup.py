from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="timmysmalls-pypipackage",
    description="This is a demo package. Please use. I'm sure you'll find it riveting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Timmysmalls",
    author_email="timothy@bttrcode.nl",
    url="https://github.com/timmysmalls/pypipackage",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=["Django"],
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
