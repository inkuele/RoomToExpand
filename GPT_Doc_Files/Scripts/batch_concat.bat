@echo off
:: Navigate to the root directory (one level up from the Scripts folder)
cd /d "%~dp0\.."

:: Loop through each .dir directory in the root folder
for /d %%d in (TD_Patch_Files/*.dir) do (
    echo Processing directory: %%d
    python Scripts\concat_dir_files.py "%%d"
)

echo Done processing all directories.
pause
