#!/usr/bin/bash
#File paths to check if installed before hand
PEDAFILE=/usr/bin/gdb-peda
PWNDBGFILE=/usr/bin/gdb-pwndbg

#Menu and reading input
printf "Choose which one to install:\n1.Peda\n2.Pwndgb\n3.Uninstall Peda and Pwndbg\n4.Exit\n"
read input

case $input in
  1) 
    #Checks if PEDA is installed else it installs it
    if [ -f "$PEDAFILE" ]; 
    then 
      printf "Peda is already installed if broken install manually.\n"
    else
      cd ~/
      touch .gdbinit
      printf "define init-peda\nsource ~/peda/peda.py\nend\ndocument init-peda\nInitializes the PEDA (Python Exploit Development Assistant for GDB) framework\nend\n\n" >> ~/.gdbinit
      
      #permissions and allows us to use gdb-peda in the terminal
      cd /usr/bin
      sudo touch gdb-peda
      sudo chmod 777 gdb-peda
      sudo printf "#!/bin/sh\nexec gdb -q -ex init-peda \"\$@\"" > gdb-peda 
      sudo chmod +x /usr/bin/gdb-*
      cd ~/CTFStuff
      printf "Finished installing peda, use gdb-peda to test.\n"
    fi
    ;;
  2)
    #Checks if Pwndbg is installed else it installs it
    if [ -f "$PWNDBGFILE" ];
    then
      printf "Pwndbg is already installed if broken install manually\n"
    else
      cd pwndbg
      chmod +x ./setup.sh
      ./setup.sh

      cd ..
      cp -r pwndbg ~/pwndbg-src
      echo "source ~/pwndbg-src/gdbinit.py" > ~/.gdbinit_pwndbg
      cd ~/
      touch .gdbinit
      printf "define init-pwndbg\nsource ~/.gdbinit_pwndbg\nend\ndocument init-pwndbg\nInitializes PwnDBG\nend\n\n" >> ~/.gdbinit
      #Removes extra garbage that it installs in this file
      sed -i 's/set debuginfod enabled on//' ~/.gdbinit
      sed -i 's/source \/home\/kappa\/CTFStuff\/pwndbg\/gdbinit.py//' ~/.gdbinit
      
      #permissions and allows us to use gdb-pwndbg in the terminal
      cd /usr/bin
      sudo touch gdb-pwndbg
      sudo chmod 777 gdb-pwndbg
      sudo printf "#!/bin/sh\nexec gdb -q -ex init-pwndbg \"\$@\"" > gdb-pwndbg
      sudo chmod +x /usr/bin/gdb-*
      cd ~/CTFStuff
      printf "Finished installing pwndbg, use gdb-pwndbg to test.\n"
    fi
    ;;
  3)
    #Uninstalling both Pwndbg and Peda
    printf "Are you sure you want to uninstall Peda or Pwndbg? (y/n)\n"
    read choice

    if [ $choice = 'y' ] || [ $choice = 'Y' ]
    then
      printf "Uninstalling...\n"
      sudo rm -rf $PEDAFILE $PWNDBGFILE ~/.gdbinit ~/pwndbg-src
      printf "Done!"
    elif [ $choice = 'n' ] || [ $choice = 'N' ]
    then
      printf "Exiting"
      exit 1
    else
      printf "Exiting"
      exit 1
    fi
    ;;
  4)
    #exits the program
    printf "Exiting";
    exit 1
    ;;
  *) 
    #If user inputs anything that isnt 1,2,3,4
    printf "Invalid Input";
    ;;
esac

