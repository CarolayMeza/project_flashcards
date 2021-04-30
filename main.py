# first main python file for project_flashcards

commands = dict()

commands['push']='EMPUJAR, este es un comando de git'
commands['select']='Seleccionar, este es un comando de SQL'
commands['dict']='diccionario, este es un comando de python'
commands['pwd']='descubrir, este es un comando de linux para saber donde estoy'
commands['from']='de, este es un comando de SQL'
commands['ls -l']='encontrar lista , este es un comando de linux'
commands['wq']='guardar y quitar cambios , este es un comando de vim'


for item in commands.items():
    print(item)  