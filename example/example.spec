# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['example.py'], # pylint: disable=undefined-variable
             pathex=['/home/shashankgopikrishna/projects/pylectron'],
             binaries=[],
             datas=[("example.html", "example.html")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, # pylint: disable=undefined-variable
             cipher=block_cipher)
exe = EXE(pyz, # pylint: disable=undefined-variable
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          Tree("electron_build", prefix="electron_build"), # pylint: disable=undefined-variable
          [],
          name='example',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
