@echo off
REM GOTO FULL
GOTO QUICK
:FULL
pip install Gooey
pip install logging
pip install requests
pip install argparse
pause

:QUICK
start "run" python redirect.py
