#You can use the sys.byteorder attribute to see the byte order of your current architecture:
import sys
sys.byteorder
# to see the size of python object
sys.getsizeof(1)
# To perform different behavior, depending on the underying os
sys.platform
# To use module that is only available to specific version of python
if sys.version_info.major < 3:
    print("You need to update your Python version")
elif sys.version_info.minor < 7:
    print("You are not running the latest version of Python")
else:
    print("All is good.")

