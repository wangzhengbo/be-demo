# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['js2py.py'],
             pathex=['/Users/wangzhengbo2/.pyenv/versions/3.7.4/lib/python3.7/site-packages', '/Users/wangzhengbo2/dev/be-demo/python/js/js2py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='js2py',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
