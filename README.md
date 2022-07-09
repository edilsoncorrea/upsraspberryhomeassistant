O objetivo desse procedimento é criar um arquivo json na pasta /dev/ com informações sobre a bateria do UPS versão Supervised.

O arquivo python foi criado a partir do arquivo disponibilizado pelo fabricante que pode ser visto [aqui]:(https://github.com/linshuqin329/UPS-18650-Lite/blob/master/UPS_18650_Lite.py)


Os arquivos deverão ser colocados na pasta `/home/pi/scripts/`

Editar o crontab: `sudo crontab -e`

Alterar os atributos do arquivo (ups_18650_lite.py)
sudo chmod +x ups_18650_lite.py

sudo /home/pi/scripts/executarpythonuos.sh

	@reboot mkdir /dev/ups
	@reboot touch /dev/ups/ups
	@reboot chmod +rw /dev/ups/ups
	* * * * *  /home/pi/scripts/executarpythonups.sh
	* * * * * sleep 20; /home/pi/scripts/executarpythonups.sh
	* * * * * sleep 40; /home/pi/scripts/executarpythonups.sh










