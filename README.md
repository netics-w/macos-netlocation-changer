# macos-netlocation-changer
This is sample project which allows you to automatically change MacOS Network Location based on Network SSID.

Sources description:

network_location.py - just parses netloc.json and returns network location name based on passed SSID arg (last arg in 
  python3.5 network_location.py netloc.json $SSID)
netloc.json - is config file with content like this:
  {
  "Network1":"Location1",
  "Network2":"Location2",
  "Network3":"Location3"
  }, where keys are SSIDs and values are your preferred Network Locations
changelocation.sh - example script for automator application creation
local.auto.change.network.location.plist - is a launchd agent which listens for 
  /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist modification
  and starting automator application after it's modification

Usage instructions:
1. Download files to your preferred location, i.e. ~/Utility/NetworkLocationChanger
2. Modify netloc.json file so your keys will be known SSIDs, and values will be Network Location Names. 
  You can find your configured network locations using Terminal command "scselect" or in 
  "System Preferences" > "Network" > "Location" 
3. Create Automator Application and use "Run Shell Script" action. Script should execute next command to return correct location for your currently connected SSID
  python3.5 network_location.py netloc.json $SSID . 
4. Paste changelocation.sh contents there. Be careful - replace path to network_location.py and netloc.json files
5. Check if application works. If not - modify scripts or config file. You can add some logging to script, i.e. add line
  echo "Changed network location at " `date` >> ~/somelogfile.log
to the end of script.
6. Save newly created automator-application to your preferred location, i.e. ~/Applications/.
7. Modify file local.auto.change.network.location.plist so that <string>/Applications/ChangeNetworkLocation.app/</string>
will point to your newly created automator application (full path). Copy it to ~/Library/LaunchAgents/
8. You can check if everything works by touching file /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist:
  touch /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist
