@echo off
echo Setting Python 3.13 as default...

REM Get current user PATH
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v Path 2^>nul') do set "USERPATH=%%b"

REM Remove old Python paths and add Python 3.13 at the beginning
setx PATH "C:\Users\lenovo\AppData\Local\Programs\Python\Python313;C:\Users\lenovo\AppData\Local\Programs\Python\Python313\Scripts;%USERPATH%"

echo.
echo Python 3.13 path has been set!
echo.
echo IMPORTANT: Please close and reopen your terminal/IDE for changes to take effect.
echo.
pause
