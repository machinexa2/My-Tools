import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-', "---", dest='stdin', action='store_true')
parser.add_argument('-w', '--wordlist', help="Wordlist")
argv = parser.parse_args()
