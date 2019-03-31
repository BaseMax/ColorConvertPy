import setuptools
with open("README.md", "r") as fh:
	Description = fh.read()
	setuptools.setup(
		name='ColorConvert',  
		version='1.0',
		scripts=['ColorConvert.py'],
	)

