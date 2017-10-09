#!/bin/bash

#Colors
cyan='\e[0;36m'
green='\e[0;32m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
blue='\e[1;34m'
#Check root exist
[[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo  $red "You must be root to run the script"; exit 1; }
echo " ______   _______ _________ _______  _______ _________ _______  _______   ";
echo "(  __  \ / ___   )\__    _/(  ____ \(  ____ \\__   __/(  ____ \(  ____ )  ";
echo "| (  \  )\/   )  |   )  (  | (    \/| (    \/   ) (   | (    \/| (    )|  ";
echo "| |   ) |    /   )   |  |  | (__    | |         | |   | (__    | (____)|  ";
echo "| |   | |   /   /    |  |  |  __)   | |         | |   |  __)   |     __)  ";
echo "| |   ) |  /   /     |  |  | (      | |         | |   | (      | (\ (     ";
echo "| (__/  ) /   (_/\|\_)  )  | (____/\| (____/\   | |   | (____/\| ) \ \__  ";
echo "(______/ (_______/(____/   (_______/(_______/   )_(   (_______/|/   \__/v2.0 ";
echo "                      Setup Script for Dzjecter v2.0 "       
echo -e $green "[ ! ] Moving Dzjecter folder "
mkdir /usr/share/Dzjecter
cp Dzjecter.py /usr/share/Dzjecter
echo -e $blue "[ ✔ ]Done"
echo "installing requirements...."
pip install -r requirements.txt
echo -e $yellow "[ ! ]  Creating shortcut command Dzjecter"
echo "#!/bin/sh" >> /usr/bin/Dzjecter
echo "cd /usr/share/Dzjecter" >> /usr/bin/Dzjecter
echo "exec python Dzjecter.py \"\$@\"" >> /usr/bin/Dzjecter
chmod +x /usr/bin/Dzjecter
echo -e $green ""
echo "------------------------------------" 
echo "| [ ✔ ]installation completed[ ✔ ] |" 
echo "------------------------------------" 
echo
echo -e $green "#####################################"
echo -e $blue "|Now Just Type In Terminal (Dzjecter)|"
echo -e $green "#####################################"
exit
