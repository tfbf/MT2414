from setuptools import setup

setup(name="matthew2414",
    version="0.1.0",
    install_requires="nltk",
    entry_points={
        "console_scripts": [
            "matthew2414-extract = matthew2414.convert:main",
            "matthew2414-convert = matthew2414.convert:main",
            ]
        }
    )
