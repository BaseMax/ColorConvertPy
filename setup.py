###
#
# @Name : Setup.py
# @Version : 1.0
# @Programmer : Max
# @Date : 2019-03-31
# @Released under : https://github.com/BaseMax/ColorConvertPy/blob/master/LICENSE
# @Repository : https://github.com/BaseMax/ColorConvertPy
#
###

import setuptools
with open("README.md", "r") as fh:
	Description = fh.read()
	setuptools.setup(
		name="ColorConvert",  
		version="1.0",
		scripts=["ColorConvert.py"],
		url="https://github.com/BaseMax/ColorConvertPy",
		packages=setuptools.find_packages(),
		author="Max Base",
		author_email="MaxBaseCode@Gmail.Com",
		description="Tiny library to convert various colored units (rgb, hex).",
		long_description=Description,
		long_description_content_type="text/markdown",
		classifiers=[
			"Programming Language :: Python :: 2",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		],
	)

