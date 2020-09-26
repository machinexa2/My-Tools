#!/usr/bin/python3

from termcolor import colored
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor

from lib.Globals import ColorObj
from lib.Functions import starter, get_cert_data
from lib.Functions import write_output, write_output_directory

parser = ArgumentParser(description=colored('Extract data from SSL/TLS certificates', color='yellow'), epilog=colored("Enjoy bug hunting", color='yellow'))
input_group = parser.add_mutually_exclusive_group()
output_group = parser.add_mutually_exclusive_group()
input_group.add_argument('---', '---', dest='stdin',  action="store_true", help='Input from stdin')
input_group.add_argument('-d', '--domain', type=str, help="Domain")
input_group.add_argument('-w', '--wordlist', type=str, help='Wordlist (subdomains)')
output_group.add_argument('-oD', '--output-directory', type=str, help="Output file directory")
output_group.add_argument('-o', '--output', type=str, help="Output file")
parser.add_argument('-t', '--threads', type=int, help="Number of threads")
parser.add_argument('-b', '--banner', action="store_true", help="Print banner and exit")
argv = parser.parse_args()

input_wordlist = starter(argv)
orgs = set()
commons = set()

with ThreadPoolExecutor(max_workers=argv.threads) as Submitter:
    try:
        future_objects = [Submitter.submit(get_cert_data, subdomain) for subdomain in input_wordlist]
    except KeyboardInterrupt:
        print(f"{ColorObj.bad} Keyboard Interrupt Detected. Aborting")
        exit()
    except Exception as E:
        print(E)
    for future_object in future_objects:
        common, org = future_object.result()
        commons.update([common])
        orgs.update([org])

if argv.output_directory:
    write_output_directory(argv.output_directory, argv.domain, orgs, commons)
if argv.output:
    write_output(argv.output, orgs, commons)
