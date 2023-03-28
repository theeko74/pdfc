@echo OFF

rem Compres all in current folder and it's subfolders
rem
rem This Windows command/script will iterate through all PDF files in the current dirrectory and all of its subdirectories.
rem It assumes that you've added the path to pdf_compressor.py to the PATH variable.
rem If the symbolic link is also set, then change the pdf_compressor.py in the command for pdfc.

FOR /F "delims=" %%G IN ('dir /s /b ^| findstr "".pdf""') DO (echo %%G & python pdf_compressor.py -o "%%G" -c 4 "%%G" & echo;)