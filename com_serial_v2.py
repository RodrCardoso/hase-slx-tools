import serial
import time

# Configurações da porta serial (ajuste para a porta correta do seu dispositivo)
porta_serial = '/dev/ttymxc0'  # Substitua pela porta serial correta
baud_rate = 115200

try:
    # Abre a porta serial
    with serial.Serial(porta_serial, baud_rate, timeout=1) as ser:
        print("Enviando comando 'ue MC'...")

        # Envia o comando "GET_IP" e espera pela resposta
        ser.write(b'ue\n')  # Envia o comando com uma nova linha
        time.sleep(0.5)         # Dá um tempo para o dispositivo responder

        # Lê a resposta
        while ser.readline() != '':
            resposta = ser.readline().decode('utf-8').strip()
            if 'ue MC' in resposta:
                print("Resposta recebida:", resposta)
            else:
                ser.write(b'ue\n')  # Envia o comando com uma nova lin
                time.sleep(0.5)         # D   um tempo para o dispositivo responder
            #    print("Nenhuma resposta recebida.")

except serial.SerialException as e:
    print(f"Erro de comunicação serial: {e}")
