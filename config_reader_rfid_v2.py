import serial
import time

# Configurações da porta serial (ajuste para a porta correta do seu dispositivo)
porta_serial = '/dev/ttymxc0'  # Substitua pela porta serial correta
baud_rate = 115200
comandos = ['ub ping 0', 'uebridge 1', 'test sen']

for comando in comandos:
    try:
        # Abre a porta serial
        with serial.Serial(porta_serial, baud_rate, timeout=1) as ser:
            print(f"Enviando comando '{comando}'...")
            c = f'{comando}\n'.encode('utf-8')  # Converte o comando para bytes com nova linha

            # Envia o comando
            ser.write(c)
            time.sleep(1)  # Aguarda o dispositivo processar o comando

            # Lê todas as linhas da resposta
            resposta = []
            while True:
                linha = ser.readline().decode('utf-8').strip()
                if not linha:  # Sai do loop quando não há mais dados
                    break
                resposta.append(linha)
            
            # Verifica e imprime a resposta
            if resposta:
                print("Resposta recebida:")
                for linha in resposta:
                    print(linha)
            else:
                print("Nenhuma resposta recebida.")

    except serial.SerialException as e:
        print(f"Erro de comunicação serial: {e}")
