# upsraspberryhomeassistant
Criar arquivo json a partir de leituras no UPS para disponibilizar para o Home Assistant versão Supervised


sudo crontab -e


sudo chmod +x ups_18650_lite.py

sudo /home/pi/scripts/executarpythonuos.sh

@reboot mkdir /dev/ups
@reboot touch /dev/ups/ups
@reboot chmod +rw /dev/ups/ups
* * * * *  /home/pi/scripts/executarpythonups.sh
* * * * * sleep 20; /home/pi/scripts/executarpythonups.sh
* * * * * sleep 40; /home/pi/scripts/executarpythonups.sh
