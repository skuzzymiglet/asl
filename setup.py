import setuptools

long_description = open("README.md", "r").read()

setuptools.setup(
        name="asl-screenlapse",
        version="0.0.0",
        author="skuzzymiglet",
        author_email="skuzzymiglet@gmail.com",
        description="a resource-inexpensive way to create timelapses from your screen",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/skuzzymiglet/asl",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: POSIX :: Linux"
            ]
        )
