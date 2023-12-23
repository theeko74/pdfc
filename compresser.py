import argparse
import os.path
import shutil
import subprocess
import sys


def compress(input_file_path, output_file_path, power=0):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: "/default",
        1: "/prepress",
        2: "/printer",
        3: "/ebook",
        4: "/screen"
    }

    # Basic controls
    # Check if valid path
    if not os.path.isfile(input_file_path):
        print("Error: invalid path for input PDF file.", input_file_path)
        sys.exit(1)

    # Check compression level
    if power < 0 or power > len(quality) - 1:
        print("Error: invalid compression level, run pdfc -h for options.", power)
        sys.exit(1)

    # Check if file is a PDF by extension
    if input_file_path.split('.')[-1].lower() != 'pdf':
        print(f"Error: input file is not a PDF.", input_file_path)
        sys.exit(1)

    flag, gs = get_ghostscript_path()
    if not flag:
        return flag, gs, 0
    print("Compress PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call(
        [
            gs,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS={}".format(quality[power]),
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            "-sOutputFile={}".format(output_file_path),
            input_file_path,
        ]
    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is {0:.5f}MB".format(final_size / 1000000))
    print("Done.")
    return True, ratio, final_size / 1000000


def get_ghostscript_path():
    try:
        if os.path.isfile('path_to_gs.txt'):
            f = open('path_to_gs.txt', 'r')
            pth = f.readline()
            f.close()
            return True, pth
        gs_names = ["gs", "gswin32", "gswin64", "gswin32c"]
        for name in gs_names:
            if shutil.which(name):
                return True, shutil.which(name)
        raise FileNotFoundError(
            f"No GhostScript executable was found on path ({'/'.join(gs_names)})"
        )
    except:
        return False, 'Error in Ghostscript connection'


def main(input_path, output_path='temp.pdf', remove=False, compress_lvl=2):
    flag, ratio, size = compress(input_path, output_path, power=compress_lvl)

    
    if remove:
        os.remove(output_path)
    
    return flag, ratio, size 
