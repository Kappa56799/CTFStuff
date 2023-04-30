#!/usr/bin/bash
cd pwndbg
chmod +x ./setup.sh
./setup.sh
cd ..
cp -r pwndbg ~/pwndbg-src
echo "source ~/pwndbg-src/gbinit.py" > ~/.gbinit_pwndbg
cd ~/
touch .gbinit

printf "define init-pwndbg\nsource ~/.gbinit_pwndbg\nend\ndocument init-pwndbg\nInitializes PwnDBG\nend" > ~/.gbinit
cd /usr/bin
sudo touch gdb-pwndbg
sudo chmod 777 gdb-pwndbg
sudo printf "#!/bin/sh\nexec gdb -q -ex init-pwndbg \"\$@\"" > gdb-pwndbg
sudo chmod +x /usr/bin/gdb-*

cd ~/CTFStuff
