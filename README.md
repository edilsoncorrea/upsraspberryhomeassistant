O objetivo desse procedimento é criar um arquivo json na pasta /dev/ com informações sobre a bateria do UPS (módulo de baterias 18650) versão Supervised do Home Assistant.

O arquivo python foi criado a partir do arquivo `UPS_18650_Lite_v1.1.py`  disponibilizado pelo fabricante que pode ser visto [aqui](https://github.com/linshuqin329/UPS-18650-Lite)


Os arquivos deverão ser colocados na pasta `/home/pi/scripts/`

Alterar os atributos do arquivo [ups_18650_lite.py](./ups_18650_lite.py)
sudo chmod +x ups_18650_lite.py

Editar o crontab: `sudo crontab -e`

Ele vai conter instruções para criação de uma pasta ups dentro da pasta do sistema /dev.

O comando touch cria um arquivo vazio na pasta recém criada /dev/ups/. Em seguida são alterados os atributos desse arquivo para que possa ser escrito. As instruções seguintes criam "timers" para chamar o batch  [executarpythonups.sh](./executarpythonups.sh) que executa o python [ups_18650_lite.py](./ups_18650_lite.py) periodicamente


	@reboot mkdir /dev/ups
	@reboot touch /dev/ups/ups
	@reboot chmod +rw /dev/ups/ups
	* * * * *  /home/pi/scripts/executarpythonups.sh
	* * * * * sleep 20; /home/pi/scripts/executarpythonups.sh
	* * * * * sleep 40; /home/pi/scripts/executarpythonups.sh










