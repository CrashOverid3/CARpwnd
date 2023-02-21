from setuptools import setup

setup(
        name="carpwnd",
        version="0.2",
        package=setuptools.find_packages(),
        install_requires=["click"],
        extras_require={}
        entry_points={
            "console_scripts": [
            "carpwnd = carpwnd.main:cli",
            ],
        }
)
