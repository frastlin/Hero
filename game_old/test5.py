import sys, os

#method1, prints "nt" for windows
print os.name

#method 2
print sys.platform
if 'win' in sys.platform:
	print "This is a windows"
else:
	print "not a windows"
"""
Here are all the major platforms. It goes:
human name
sys.platform name

Linux (2.x and 3.x)
'linux2'
Windows
'win32'
Windows/Cygwin
'cygwin'
Mac OS X
'darwin'
OS/2
'os2'
OS/2 EMX
'os2emx'
RiscOS
'riscos'
AtheOS
'atheos'

so windows is win32
"""
