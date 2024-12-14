#!/bin/bash

show_help() {
    echo
	echo "Usage $0 <DOMAIN> <WORDLIST> <URL> <FS_FILTER>"
    echo "   -h, --help     Display this help and exit"
    echo
	echo "Ffuf subdomain syntax is forgettable."
}

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
	show_help
	exit 0
fi

if [ "$#" -ne 4 ]; then
	echo "Error: Missing parameter..."
	show_help
	exit 1
fi

DOMAIN="$1"
WORDLIST="$2"
URL="$3"
FS="$4"

echo "$DOMAIN"
echo "$WORDLIST"
echo "$URL"
echo "$FS"

ffuf -H "Host: FUZZ.$DOMAIN" -c -w $WORDLIST -u $URL -fs $FS
