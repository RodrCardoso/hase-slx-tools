import serial
import time

# Configura    es da porta serial (ajuste para a porta correta do seu dispositivo)
porta_serial = '/dev/ttymxc0'  # Substitua pela porta serial correta
baud_rate = 115200

comandos = ['ping', 'ping 0', 'ping 1', 'ping 2', 'ping 3', 'ping 4', 'ping 5', 'ping 6', 'get', 'get tcpip', 'get tcpport', 'getv']
#comandos = ['ping', 'setv ethcfg 1', 'get tcpip', 'sdec hFFFFF3 h01010101010101010101010101010101']
#comandos = ['get UNIQUEID', 'get FWVER', 'get T', 'get UPTIME', 'get checksum', 'get stimestamp', 'get overwrts', 'get tcpip', 'get tcpport', 'get uhfsftime', 'getok']

comandos = ['set tcpip 192.168.3.150',
            'set tcpport 2189',
            'set uhfreader 1',
            'set uhfcfg 0 attrib ants=1',
            'set uhfcfg 1 attrib fs=26db,1db,1db,1db',
            'set uhfcfg 2 attrib rdtries=4',
            'set uhfcfg 3 attrib rpttimeout=0',
            'set uhfcfg 4 attrib idtimeout=0',
            'set uhfcfg 5 attrib anttimeout=0',
            'set uhfcfg 6 attrib idtries=1',
            'set uhfcfg 7 attrib anttries=2',
            'set uhfcfg 8 attrib seltries=1',
            'set uhfcfg 9 attrib unseltries=0',
            'set uhfcfg 10 attrib inittries=1',
            'set uhfcfg 11 attrib initialq=0',
            'set uhfcfg 12 attrib querysel=4',
            'set uhfcfg 13 attrib querytarget=a',
            'set uhfcfg 14 attrib session=2',
            'set uhfcfg 15 attrib epcc1g2parms=12',
            'set uhfcfg 16 attrib schedopt=2',
            'set uhfcfg 17 attrib notagrpt=off',
            'set uhfcfg 18 attrib idreport=on',
            'setv ethcfg 1']


#EDGE60R
#comandos = ['set tcpip 192.168.15.165', 'set tcpport 8080', 'set uhfreader 0', 'setv ethcfg 1', 'get tcpip', 'sdec hFFFFF3 h01010101010101010101010101010101']
#comandos BLE
comandos = ['ub ping 0', 'uebridge 1', 'test sen', 'ub get']

#comandos = ['setv ethcfg 1']
#comandos = ['del all']

for comando in comandos:
    try:
        # Abre a porta serial
        with serial.Serial(porta_serial, baud_rate, timeout=1) as ser:
            print(f"Enviando comando '{comando}'...")
            c = f'{comando}\n'.encode('utf-8')  # Converte o comando para bytes com nova linha
            #print(teste)
            # Envia o comando "GET_IP" e espera pela resposta
            ser.write(c)
            #ser.write(b'ping\n')  # Envia o comando com uma nova linha
            time.sleep(1)         # D   um tempo para o dispositivo responder
            #print(ser.readline().decode('utf-8'))
            # L   a resposta
            resposta = ser.readline().decode('utf-8').strip()
            if resposta:
                print("Resposta recebida:", resposta)
            else:
                print("Nenhuma resposta recebida.")

    except serial.SerialException as e:
        print(f"Erro de comunica    o serial: {e}")



