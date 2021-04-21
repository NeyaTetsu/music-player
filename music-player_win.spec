# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['music-player.py'],
             pathex=['C:\\Users\\user\\Desktop\\music-player'],
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
a.datas += [('asset/pause.png', '.\\asset\\pause.png', 'DATA'),
            ('asset/play.png', '.\\asset\\play.png', 'DATA'),
            ('asset/refresh-sharp.png', '.\\asset\\refresh-sharp.png', 'DATA'),
            ('asset/stop.png', '.\\asset\\stop.png', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.datas,
          name='music-player',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon='music-player.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='music-player')
