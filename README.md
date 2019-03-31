# Color Convert Python

## Sample

#### Import

```python
from ColorConvert import *
```

### Using

```python
hex = rgb2hex((255,255,255))
print( hex ) # FFFFFF
print( hex2rgb( hex ) ) # (255, 255, 255)
```

## Install

**$ sudo python setup.py install**

```
running install
running bdist_egg
running egg_info
creating ColorConvert.egg-info
writing ColorConvert.egg-info/PKG-INFO
writing top-level names to ColorConvert.egg-info/top_level.txt
writing dependency_links to ColorConvert.egg-info/dependency_links.txt
writing manifest file 'ColorConvert.egg-info/SOURCES.txt'
reading manifest file 'ColorConvert.egg-info/SOURCES.txt'
writing manifest file 'ColorConvert.egg-info/SOURCES.txt'
installing library code to build/bdist.freebsd-12.0-RELEASE-amd64/egg
running install_lib
warning: install_lib: 'build/lib' does not exist -- no Python modules to install

creating build
creating build/bdist.freebsd-12.0-RELEASE-amd64
creating build/bdist.freebsd-12.0-RELEASE-amd64/egg
creating build/bdist.freebsd-12.0-RELEASE-amd64/egg/EGG-INFO
installing scripts to build/bdist.freebsd-12.0-RELEASE-amd64/egg/EGG-INFO/scripts
running install_scripts
running build_scripts
creating build/scripts-2.7
copying and adjusting ColorConvert.py -> build/scripts-2.7
changing mode of build/scripts-2.7/ColorConvert.py from 644 to 755
creating build/bdist.freebsd-12.0-RELEASE-amd64/egg/EGG-INFO/scripts
copying build/scripts-2.7/ColorConvert.py -> build/bdist.freebsd-12.0-RELEASE-amd64/egg/EGG-INFO/scripts
changing mode of build/bdist.freebsd-12.0-RELEASE-amd64/egg/EGG-INFO/scripts/ColorConvert.py to 755
copying ColorConvert.egg-info/PKG-INFO -> build/bdist.freebsd-12.0-RELEASE-amd64/egg/EGG-INFO
copying ColorConvert.egg-info/SOURCES.txt -> build/bdist.freebsd-12.0-RELEASE-amd64/egg/EGG-INFO
copying ColorConvert.egg-info/dependency_links.txt -> build/bdist.freebsd-12.0-RELEASE-amd64/egg/EGG-INFO
copying ColorConvert.egg-info/top_level.txt -> build/bdist.freebsd-12.0-RELEASE-amd64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/ColorConvert-1.0-py2.7.egg' and adding 'build/bdist.freebsd-12.0-RELEASE-amd64/egg' to it
removing 'build/bdist.freebsd-12.0-RELEASE-amd64/egg' (and everything under it)
Processing ColorConvert-1.0-py2.7.egg
Copying ColorConvert-1.0-py2.7.egg to /usr/local/lib/python2.7/site-packages
Adding ColorConvert 1.0 to easy-install.pth file
Installing ColorConvert.py script to /usr/local/bin

Installed /usr/local/lib/python2.7/site-packages/ColorConvert-1.0-py2.7.egg
Processing dependencies for ColorConvert==1.0
Finished processing dependencies for ColorConvert==1.0
```
