import serial
import time

# Configura    es da porta serial (ajuste para a porta correta do seu dispositivo)
porta_serial = '/dev/ttymxc0'  # Substitua pela porta serial correta
baud_rate = 115200
#bancada 10.128.15.210
#portico vb 192.168.3.150
#IF2
#comandos = ['set tcpip 10.128.15.210',
comandos = ['set tcpip 192.168.3.150',
            'set tcpport 2189',
            'set uhfreader 1',
            'set uhfcfg 0 attrib ants=1',
            'set uhfcfg 1 attrib fs=28db,1db,1db,1db',
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
            'set uhfcfg 17 attrib notagrpt=on',
            'set uhfcfg 18 attrib idreport=on',
            'setv ethcfg 1']


#EDGE60R
#comandos = ['set tcpip 192.168.15.165', 'set tcpport 8080', 'set uhfreader 0', 'setv ethcfg 1', 'get tcpip', 'sdec hFFFFF3 h01010101010101010101010101010101']
#comandos BLE
comandos = ['get']
#deleta as configuracoes
#comandos = ['del all', 'setv ethcfg 1', 'getv', 'get tcpip']
#comandos = ['setv ethcfg 1', 'get']
comandos = ['ub ping 0', 'ub get', 'get']

for comando in comandos:
    try:
        # Abre a porta serial
        with serial.Serial(porta_serial, baud_rate, timeout=1) as ser:
            print(f"Enviando comando '{comando}'...")
            c = f'{comando}\n'.encode('utf-8')  # Converte o comando para bytes com nova linha

            # Envia o comando
            ser.write(c)
            time.sleep(1)  # Aguarda o dispositivo processar o comando

            # L   todas as linhas da resposta
            resposta = []
            t = 0
            while t < 60:
                linha = ser.readline().decode('utf-8').strip()
                if 'ok' in linha:  # Sai do loop quando n  o h   mais dados
                    resposta.append(linha)
                    break
                #if 'UHF1' not in linha or 'HTB0' not in linha:
                resposta.append(linha)
                t += 1

            # Verifica e imprime a resposta
            if resposta:
                print("Resposta recebida:")
                for linha in resposta:
                    print(linha)
            else:
                print("Nenhuma resposta recebida.")

    except serial.SerialException as e:
        print(f"Erro de comunica    o serial: {e}")
