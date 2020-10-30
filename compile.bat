:: Set this file for compiling the executable.
:: So it can be added to the user custom theme in solidedge.
ipyc.exe /main:__main__.py ^
replace.py ^
Interop.SolidEdge.dll ^
/embed ^
/out:change_background ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:icon.ico
