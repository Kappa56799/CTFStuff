#!/usr/bin/bash
#
#Enter Directory and install gdb-pwndbg
cd pwndbg
chmod +x ./setup.sh
./setup.sh

#copy files over and create a blank .gbinit file
cd ..
cp -r pwndbg ~/pwndbg-src
echo "source ~/pwndbg-src/gbinit.py" > ~/.gbinit_pwndbg #redirect source into file
cd ~/
touch .gbinit
printf "define init-pwndbg\nsource ~/.gbinit_pwndbg\nend\ndocument init-pwndbg\nInitializes PwnDBG\nend" > ~/.gbinit #redirect this into the file

#Make a new file to allow us to use gdb-pwndbg in terminal
cd /usr/bin
sudo touch gdb-pwndbg
sudo chmod 777 gdb-pwndbg
sudo printf "#!/bin/sh\nexec gdb -q -ex init-pwndbg \"\$@\"" > gdb-pwndbg #redirect this into the file
sudo chmod +x /usr/bin/gdb-*
cd ~/CTFStuff #return back
