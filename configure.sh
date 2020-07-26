#!/usr/bin/env sh
<< 'APP-ID-REF'
17520   Synergy
220     Half-Life 2
380     Half-Life 2: Episode One
420     Half-Life 2: Episode Two
340     Half-Life 2: Lost Coast
APP-ID-REF

yum install -y glibc.i686 libstdc++.i686
useradd -m steam

su steam <<'EOF'
mkdir ~/Steam && cd ~/Steam
wget 'http://media.steampowered.com/installer/steamcmd_linux.tar.gz'
tar -xzvf steamcmd_linux.tar.gz && rm -f steamcmd_linux.tar.gz
echo "
@ShutdownOnFailedCommand 0
@NoPromptForPassword 1
login anonymous 
app_update 17520 validate
app_update 220 validate
app_update 380 validate
app_update 420 validate
app_update 340 validate
quit" > synergy.txt
./steamcmd.sh +runscript synergy.txt
EOF

