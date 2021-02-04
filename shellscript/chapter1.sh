#condition check []
clear
echo pwd
touch file1 file2
mkdir sada
cd sada
touch readme.txt
    echo "This is my readme file">>readme.txt
cd ..
echo "Hello, $USER"
echo "list file in current directory"
ls
echo "System uptime"
uptime
echo "Today's date is `date`, this is week `date +"%V"`."
echo
echo "These users are currently connected:"
w | cut -d " " -f 1 - | grep -v USER | sort -u
echo
printf  "This is `uname -s` running on a `uname -m` processor.\n\n"
tar -zxvf downloads/dist/boto-2.5.2.tar.gz

# This script is for /etc/rc.d/init.d
# Link in rc3.d/S99audio-greeting and rc0.d/K01audio-greeting

case "$1" in
'start')
    cat /usr/share/audio/at_your_service.au > /dev/audio
    ;;
'stop')
    cat /usr/share/audio/oh_no_not_again.au > /dev/audio
    ;;
    esac
    exit 0

