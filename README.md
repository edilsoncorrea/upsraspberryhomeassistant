# Como instalar o Módulo UPS 18650 no Raspberry e Utilizar os dados de bateria no Home Assistant

O objetivo desse procedimento é criar um arquivo json na pasta /dev/ com informações sobre a bateria do UPS (módulo de baterias 18650) versão Supervised do Home Assistant.

O arquivo python foi criado a partir do arquivo [ups_18650_lite.py](ups_18650_lite.py)  disponibilizado pelo fabricante que pode ser visto [aqui](https://github.com/edilsoncorrea/UPS-18650-Lite)


Os arquivos deverão ser colocados na pasta `/home/pi/scripts/`

Alterar os atributos do arquivo [ups_18650_lite.py](./ups_18650_lite.py)
sudo chmod +x ups_18650_lite.py

Editar o crontab: `sudo crontab -e`

Ele vai conter instruções para criação de uma pasta ups dentro da pasta do sistema /dev.

O comando touch cria um arquivo vazio na pasta recém criada /dev/ups/. Em seguida são alterados os atributos desse arquivo para que possa ser escrito. As instruções seguintes criam "timers" para chamar o batch [executarpythonups.sh](./executarpythonups.sh) que executa o python [ups_18650_lite.py](./ups_18650_lite.py) periodicamente

````
	@reboot mkdir /dev/ups
	@reboot touch /dev/ups/ups
	@reboot chmod +rw /dev/ups/ups
	* * * * *  /home/pi/scripts/executarpythonups.sh
	* * * * * sleep 20; /home/pi/scripts/executarpythonups.sh
	* * * * * sleep 40; /home/pi/scripts/executarpythonups.sh
````

No Home Assistant para ler os dados que são gravados no Json é necessário criar esses sensores no Configuration.yaml

````

  - platform: command_line
    name: UPS 18650 Lite
    scan_interval: 10
    command_timeout: 30
    json_attributes:
      - capacidade
      - voltagem
    value_template: "{{ value_json.estado }}"
    command: "cat /dev/ups/ups"
    unique_id: ups_18650_lite
    
  - platform: template
    sensors: 
      voltagem_bateria_raspberry:
        value_template: '{{ states.sensor.ups_18650_lite.attributes.voltagem|round(2) }}'
        friendly_name: "Voltagem Bateria Raspberry"
        unit_of_measurement: "V"
        unique_id: voltagem_bateria_raspberry
    
      capacidade_bateria_raspberry:
        value_template: '{{ states.sensor.ups_18650_lite.attributes.capacidade|round(2) }}'
        friendly_name: "Capacidade Bateria Raspberry"
        unit_of_measurement: "%"
        unique_id: capacidade_bateria_raspberry
	
````	








