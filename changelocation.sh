#!/bin/bash
SSID=`/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep ' SSID' | awk '{print $2}'`
#You should provide full path to 
#	network_location.py - script which returns network location name
#	netloc.json - config file which contains SSID - Location matching
location=`python3.5 network_location.py netloc.json $SSID`
scselect $location
