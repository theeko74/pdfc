Pdfc --  PDF Compressor
=======================

Simple python script to compress PDF.

Installation
-------------
* Install dependency Ghostscript.
On MacOSX: `brew install ghostscript`
On Windows: install binaries via [official website] (https://www.ghostscript.com/)
* Create a symbolic link if you want to run it everywhere in bash
`ln -s pdf_compressor.py pdfc`
* Add in PATH environment variable
On MacOSX:
`echo 'export PATH="/absolute/path/of/the/folder/script/:$PATH"' >> ~/.bash_profile`

Usage
-----
`pdfc [-o output_file_path] [-c number] input_file_path`

Ex:
`pdfc -o out.pdf in.pdf`

Output:
```
Compress PDF...
Compression by 65%.
Final file size is 1.4MB
Done.
```

Options
-------
* `-c` or `--compress` specifies 5 levels of compression, similar to standard pdf generator level:
  * 0: default - *almost identical to /screen*
  * 1: prepress - *high quality, color preserving, 300 dpi imgs*
  * 2: printer - *high quality, 300 dpi images*
  * 3: ebook - *low quality, 150 dpi images*
  * 4: screen - *screen-view-only quality, 72 dpi images*
* `-o`or `--out` specifies the output file path. If not specified, input file will be erased.
* `-b`or `--backup` creates a backup of the original file in case no output is specified to avoid erasing the original file.
