import setuptools
import os

long_description = open(os.path.join(os.path.dirname(__file__), "README.rst"), "r", encoding="utf-8").read()

setuptools.setup(
    name="asl-screenlapse",
    version="0.1.3",
    author="skuzzymiglet",
    author_email="skuzzymiglet@gmail.com",
    description="a resource-inexpensive way to create timelapses from your screen",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skuzzymiglet/asl",
    packages=["asl"],
    setup_requires=["pyscreenshot", "pyautogui"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
        ],
    entry_points={
        'console_scripts': [
            'asl=asl.asl:main',
            'asl-timelapse=asl.timelapse:main'
            ],
        }
)
