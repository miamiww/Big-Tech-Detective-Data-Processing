#!/bin/bash

############################################################################################################
# ----------------------------------------------------------------------
# ASN/IPv4/Prefix lookup tool. Uses Team Cymru's whois service for data.
# ----------------------------------------------------------------------
# example usage:
#  asn <ASnumber>      -- to lookup matching ASN data. Supports "as123" and "123" formats (case insensitive)
#  asn <IP.AD.DR.ESS>  -- to lookup matching route and ASN data
#  asn <ROUTE>         -- to lookup matching ASN data
#  asn <host.name.tld> -- to lookup matching IP, route and ASN data (supports multiple IPs - e.g. DNS RR)
#
# Author: Adriano Provvisiero - BV Networks 2017
#
############################################################################################################

WhoisASN(){
        found_asname=$(whois -h whois.cymru.com " -f -w -c -p as$1" | sed -e 's/\ *|\ */|/g' | awk -F '[|]' {'print $3'})
        printf "$red[AS$1] $green$found_asname\n$white"
}

WhoisIP(){
        printf "$white%15s -> $yellow(route: %18s) $white-> $red[AS%s] $green%s\n" "$1" "$found_route" "$found_asn" "$found_asname"
}

LookupASNAndRouteFromIP(){
        found_route=""
        found_asn=""
        found_asname=""
        output=$(whois -h whois.cymru.com " -f -p $1" | sed -e 's/\ *|\ */|/g')
        found_asn=$(echo $output | awk -F'[|]' {'print $1'})
        found_asname=$(echo $output | awk -F'[|]' {'print $4'})
        found_route=$(echo $output | awk -F'[|]' {'print $3'})
}

ResolveHostnameToIPList(){
        ip=$(host $1 | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
        echo -e "$ip\n"
}

green="\e[32m"
yellow="\e[33m"
white="\e[97m"
blue="\e[94m"
red="\e[31m"

input=$(echo $1 | sed -e 's/\/.*//g' | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
if [ -z "$input" ]; then
        # Input is not an IPv4 Address. Check if it is a number (ASN)
        asn=$(echo $1 | sed -e 's/[a|A][s|S]//g' | grep -E "^[0-9]*$")
        if [ -z "$asn" ]; then
                # Input is not an ASN either. Consider it a hostname and try to resolve it.
                echo -e -n "${blue}Resolving \"$1\"... "
                ip=$(ResolveHostnameToIPList $1)
                if [ -z "$ip" ]; then
                        echo -e "\e[97m\e[101mError: unable to resolve hostname\e[39m\e[49m"
                        tput sgr0
                        exit
                fi
                numips=$(echo "$ip" | wc -l)
                [[ $numips = 1 ]] && s="" || s="es"
                echo -e "$blue$numips IP address$s found:"
                for singleip in $ip; do
                        LookupASNAndRouteFromIP $singleip
                        WhoisIP $singleip
                done
                tput sgr0
                exit
        else
                # Input is an ASN
                WhoisASN $asn
                tput sgr0
                exit
        fi
else
        # Input is an IPv4
        LookupASNAndRouteFromIP $input
        if [ -z "$found_asname" ] && [ -z "$found_route" ]; then
                echo -e "\e[97m\e[101mError: no data found for $input\e[39m\e[49m"
                tput sgr0
                exit
        fi
        echo -e "${green}1 IP address found:\e[39m"
        WhoisIP $input
        tput sgr0
        exit
fi
