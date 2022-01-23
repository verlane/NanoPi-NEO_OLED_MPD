#! /bin/sh

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting oled_mpd"
    /usr/local/bin/oled_mpd.py &
    /usr/local/bin/oled_mpd_btn.py &
    ;;
  stop)
    echo "Stopping oled_mpd"
    pkill -f /usr/local/bin/oled_mpd.py
    pkill -f /usr/local/bin/oled_mpd_btn.py
    ;;
  *)
    echo "Usage: /etc/init.d/oled_mpd.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
