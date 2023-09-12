from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_field_prefixing/__init__.py
from custom_field_prefixing import __version__ as version

setup(
	name="custom_field_prefixing",
	version=version,
	description="App which remove or edit auto new fields prefixing with \'custom_\'",
	author="Imad Abdou",
	author_email="igentle.appletec@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
