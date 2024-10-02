@echo off
rem Set the path to your SuperCollider installation (update this if necessary)
set SC_PATH="C:\Program Files\SuperCollider-3.x.x"  rem Adjust to match your SC path

rem Set the path to the patch file
set PATCH_PATH="C:\path\to\granularPatch.scd"  rem Adjust to the location of your patch file

rem Change to the SuperCollider directory
cd /d %SC_PATH%

rem Launch SuperCollider with the patch file
start sclang.exe "%PATCH_PATH%"

