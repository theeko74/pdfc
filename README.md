PdfcGUI -  PDF Compressor (with GUI) 
=======================

Simple Python app to compress PDF with GUI.


![image](https://github.com/zaborshikov/pdfc_with_gui/assets/31626137/5b0db79f-cac5-4cc1-bf99-d6710e4d9297)

Installation
-------------
* Install Ghostscript dependency.
On MacOSX: `brew install ghostscript`
On Windows: install binaries via [official website](https://www.ghostscript.com/)
* Add to PATH environment variable
On MacOSX:
`echo 'export PATH="/absolute/path/of/the/folder/script/:$PATH"' >> ~/.bash_profile`
* Intsall flet by this comand: `pip install flet`

Usage
-----
Run gui.py

Solve the problems
-------
If you have problems with Ghostscript, you can try to make a file with name `path_to_gs.txt` and type path to `gswin32c.exe` on your PC.

Features
-------
- [ ] Another compressors
- [ ] Build EXE
- [ ] Multi-select (files)
- [ ] Improve UX&UI (add animations and PDF viewer, make adaptive interface)
- [ ] Convenient and accurate selection of compression accuracy
- [ ] Progress bar 
