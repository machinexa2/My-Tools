# Certificate Extractor

## Description
Extract organization names and domains for chaining with other tools such as Github Dorker(organizations) and subdomain scraper(domains).

## Usage
```
root@kali-linux:~/MachineYadav/My-Tools/Certex# Certex --help
usage: Certex [-h] [--- | -d DOMAIN | -w WORDLIST] [-oD OUTPUT_DIRECTORY] [-t THREADS] [-b]

Extract data from SSL/TLS certificates

optional arguments:
  -h, --help            show this help message and exit
  ---, ---              Input from stdin
  -d DOMAIN, --domain DOMAIN
                        Domain
  -w WORDLIST, --wordlist WORDLIST
                        Wordlist (subdomains)
  -oD OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
                        Output file directory
  -t THREADS, --threads THREADS
                        Number of threads
  -b, --banner          Print banner and exit

Enjoy bug hunting
```

## Example
1. Extract from single domain 
* `Certex -d google.com`
2. Extract from wordlist
* `Certex -w /path/to/wodlist -oD /tmp/ -d yahoo.com`
3. Read and extract from stdin
* `echo -ne "google.com\nyahoo.com" Certex ---`
