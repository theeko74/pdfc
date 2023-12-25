PdfcGUI -  PDF Compressor (with GUI) 
=======================

Simple python app to compress PDF with GUI.

Installation
-------------
* Install dependency Ghostscript.
On MacOSX: `brew install ghostscript`
On Windows: install binaries via [official website] (https://www.ghostscript.com/)
* Add in PATH environment variable
On MacOSX:
`echo 'export PATH="/absolute/path/of/the/folder/script/:$PATH"' >> ~/.bash_profile`
* Intsall flet by this comand: `pip install flet`

Usage
-----
Run gui.py

Solove the problems
-------
If you have problems with Ghostscript, you can try make file with name `path_to_gs.txt` and type path to `gswin32c.exe` on your PC.
