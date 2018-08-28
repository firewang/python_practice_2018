# -*- mode: python -*-

block_cipher = None


a = Analysis(['main_baidu_asr.py'],
             pathex=['E:\\pycharmProjectsHome\\python_practice_2018\\13.audio_to_text.byBaiduASR'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main_baidu_asr',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
