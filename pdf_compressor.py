#!/usr/bin/env python3
# Author: Sylvain Carlioz
# 6/03/2017
# MIT license -- free to use as you want, cheers.

"""
Simple python wrapper script to use ghoscript function to compress PDF files.

Compression levels:
    0: default
    1: prepress
    2: printer
    3: ebook
    4: screen

Dependency: Ghostscript.
On MacOSX install via command line `brew install ghostscript`.
"""

import argparse
import subprocess
import os.path
import sys
from shutil import copyfile


def compress(input_file_path, output_file_path, backup, power=0):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    # Basic controls
    # Check if valid path
    if not os.path.isfile(input_file_path):
        print("Error: invalid path for input PDF file")
        sys.exit(1)

    # Check if file is a PDF by extension
    if input_file_path.split('.')[-1].lower() != 'pdf':
        print("Error: input file is not a PDF")
        sys.exit(1)

    print("Compress PDF...")
    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                    '-dPDFSETTINGS={}'.format(quality[power]),
                    '-dNOPAUSE', '-dQUIET', '-dBATCH',
                    '-sOutputFile={}'.format(output_file_path),
                     input_file_path]
    )
    
    initial_size = os.path.getsize(input_file_path)
    final_size = os.path.getsize(output_file_path)

    # Check if compressing was resourceful
    if final_size > initial_size:
        os.remove(output_file_path)
        print("Compression not sucessfull")
    # In case no output file is specified, erase original file
    elif output_file_path == 'temp.pdf':
        if backup:
            copyfile(input_file_path, input_file_path.replace(".pdf", "_BACKUP.pdf"))
        copyfile(output_file_path, input_file_path)
        os.remove(output_file_path)

        ratio = 1 - (final_size / initial_size)
        print("Compression by {0:.0%}.".format(ratio))
        print("Final file size is {0:.1f}MB".format(final_size / 1000000))
        print("Done.")

def compress_directory(input_dir_path, backup, power=0):
    
    # Default File Path
    output_file_path = "temp.pdf"

    # The extension to search for
    exten = '.pdf'

    for dirpath, dirnames, files in os.walk(input_dir_path):
        
        for name in files:
            if name.lower().endswith(exten):
                file_path = os.path.join(dirpath, name)
                compress(file_path, output_file_path, power)
        
        for dirname in dirnames:
            new_dir_path = os.path.join(dirpath, dirname)
            compress_directory(new_dir_path, backup, power)

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input', help='Relative or absolute path of the input PDF file or directory')
    parser.add_argument('-o', '--out', help='Relative or absolute path of the output PDF file')
    parser.add_argument('-c', '--compress', type=int, help='Compression level from 0 to 4')
    parser.add_argument('-b', '--backup', action='store_true', help="Backup the old PDF file")
    parser.add_argument('--open', action='store_true', default=False,
                        help='Open PDF after compression')
    args = parser.parse_args()

    # In case no compression level is specified, default is 2 '/ printer'
    if not args.compress:
        args.compress = 2
    # In case no output file is specified, store in temp file
    if not args.out:
        args.out = 'temp.pdf'

    if os.path.isdir(args.input):
        compress_directory(args.input, args.backup, power=args.compress)
    elif os.path.isfile(args.input):
        # Run
        compress(args.input, args.out, args.backup, power=args.compress)

        # In case we want to open the file after compression
        if args.open:
            if args.out == 'temp.pdf' and args.backup:
                subprocess.call(['open', args.input])
            else:
                subprocess.call(['open', args.out])

    else:
        print("Error: invalid path for input PDF file")
        sys.exit(1)
    


if __name__ == '__main__':
    main()
