@REM GOTO FULLINSTALL
GOTO QUICKINSTALL
:FULLINSTALL
python.exe -m pip install --upgrade pip
pip install Gooey
pip install pyinstaller-versionfile
pip install hashlib
pip install logging
pip install os

REM # Exe installer:
pip install -U pyinstaller

:QUICKINSTALL
python createVersionFile.py
REM Get the version number from the const.py file
setlocal
for /f "tokens=2 delims== " %%G in ('findstr "VERSION=" const.py') do set VERSION=%%~G
@REM echo %VERSION%
@REM pyinstaller --exclude=config.ini --version-file=versionfile.txt  --icon=redirect.ico --windowed --onefile redirect\redirect.py 
@REM pyinstaller --onefile --noconfirm --clean --exclude=config.ini --exclude-module PyInstaller.main --exclude-module PyInstaller.hooks --exclude-module matplotlib.tests --exclude-module scipy.tests --exclude-module numpy.random.tests --exclude-module numpy.linalg.tests --exclude-module numpy.fft.fftpack_lite --version-file=versionfile.txt --icon=redirect.ico --windowed --onefile redirect\redirect.py

@REM No --windowed to allow console output to be shown and support CLI and GUI modes at the same time
pyinstaller --onefile --noconfirm --clean --exclude=config.ini --exclude-module PyInstaller.main --exclude-module PyInstaller.hooks --exclude-module matplotlib.tests --exclude-module scipy.tests --exclude-module numpy.random.tests --exclude-module numpy.linalg.tests --exclude-module numpy.fft.fftpack_lite --version-file=versionfile.txt --icon=redirect.ico --onefile redirect\redirect.py


set OUTPUT_FILE=dist\Redirect_v%VERSION%.zip
python -c "import zipfile, os; files_to_zip=['dist/redirect.exe', 'README.md', 'LICENSE']; zip_file=zipfile.ZipFile('%OUTPUT_FILE%', 'w'); [zip_file.write(file_to_zip, os.path.basename(file_to_zip)) for file_to_zip in files_to_zip]; zip_file.close()"