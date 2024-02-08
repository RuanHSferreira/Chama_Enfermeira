import configparser


config = configparser.ConfigParser()

config.read('config.ini')

print(config['CONFIGURACOES'])

for i in config['CONFIGURACOES']:
    print(config['CONFIGURACOES'][i].split(","))
