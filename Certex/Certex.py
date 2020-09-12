#!/usr/bin/python3
from lib.Globals import ColorObj
from lib.Functions import starter, get_cert_data
from lib.PathFunctions import PathFunction
from argparse import ArgumentParser
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor

parser = ArgumentParser(description=colored('Domain and Organization Extractor from Certificate', color='yellow'), epilog=colored("Enjoy bug hunting", color='yellow'))
parser.add_argument('-w', '--wordlist', type=str, help='Absolute path of subdomain wordlist')
parser.add_argument('-oD', '--output-directory', type=str, help="Output file directory")
parser.add_argument('-d', '--domain', type=str, help="Domain name")
parser.add_argument('-t', '--threads', type=int, help="Number of threads")
parser.add_argument('-b', '--banner', action="store_true", help="Print banner and exit")
argv = parser.parse_args()
starter(argv)

FPathApp = PathFunction()
input_data = [line.rstrip('\n') for line in open(argv.wordlist)]
output_file = open(FPathApp.slasher(argv.output_directory) + argv.domain + '.cert', 'a')
orgs = set()
commons = set()

with ThreadPoolExecutor(max_workers=argv.threads) as Submitter:
    try:
        future_objects = [Submitter.submit(get_cert_data, subdomain) for subdomain in input_data]
    except KeyboardInterrupt:
        print(f"{ColorObj.bad} Keyboard Interrupt Detected. Aborting")
        exit()
    except Exception as E:
        print(E)
    for future_object in future_objects:
        common, org = future_object.result()
        commons.update([common])
        orgs.update([org])
for org in orgs:
    print(f"{ColorObj.good} Found {org} from Certificates")
    output_file.write(org + ',')
output_file.write('\n')

for common in commons:
    print(f"{ColorObj.good} Found {common} from Certificates")
    output_file.write(common + '\n')
    output_file.close()
