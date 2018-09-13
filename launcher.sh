#!/bin/sh

# Pass in a valid ISO 3166-1 country code: ca
# Pass in multiple valid ISO 3166-1 country codes: ca do gb de fr
# Pass in default to reset torrc to factory mode: default
# Hit enter to launch Tor without any modifications.
# Closes Terminal when done.
function tor(){
    # Path to Tor root directory
    torpath='';
    # Path to tor-country root directory
    torcountry='';
    echo "Country < code(s) > or < default > or < enter > to skip:";
    read code 
    cmmd="$code";
    if [[ "${cmmd}" ]]; then
        cd "${torcountry}";
        python ./main.py "${cmmd}";
    fi
    cd "${torpath}";
    './start-tor-browser.desktop';
    exit;
}