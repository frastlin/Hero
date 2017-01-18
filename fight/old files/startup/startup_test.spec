# -*- mode: python -*-
a = Analysis(['startup_test.py'],
             pathex=["C:\\Users\\Brandon's Laptop2\\programming\\PythonFiles\\My_Games\\Hero\\fight\\startup"],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='startup_test.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
