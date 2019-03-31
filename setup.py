import setuptools
with open("README.md", "r") as fh:
	Description = fh.read()
	setuptools.setup(
		name='ColorConvert',  
		version='1.0',
		scripts=['ColorConvert.py'],
		author="Max Base",
		author_email="MaxBaseCode@Gmail.Com",
		description="Tiny library to convert various colored units (rgb, hex).",
		long_description=Description,
		long_description_content_type="text/markdown",
		url="https://github.com/BaseMax/ColorConvertPy",
		packages=setuptools.find_packages(),
	)

