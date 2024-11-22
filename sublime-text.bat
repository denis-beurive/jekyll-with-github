SET PWD=%~dp0

REM Find the path to the editor:
REM Get-Childitem –Path 'C:\Program Files' -Include subl.exe -File -Recurse -ErrorAction SilentlyContinue | Select-Object FullName | Select-String -Pattern "\\subl.exe\}?$" -AllMatches

"C:\Program Files\Sublime Text\subl.exe" %PWD%
