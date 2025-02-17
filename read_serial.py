import serial

# Configurações da porta serial (ajuste para a porta correta do seu dispositivo)
porta_serial = '/dev/ttymxc0'  # Substitua pela porta serial correta
baud_rate = 115200

try:
    # Abre a porta serial
    with serial.Serial(porta_serial, baud_rate, timeout=1) as ser:
        print("Aguardando dados na porta serial...")

        # Loop para leitura contínua
        while True:
            # Lê a resposta da serial
            resposta = ser.readline().decode('utf-8').strip()
            if resposta:  # Verifica se há dados recebidos
                print("Resposta recebida:", resposta)

except serial.SerialException as e:
    print(f"Erro de comunicação serial: {e}")
except KeyboardInterrupt:
    print("Leitura serial interrompida pelo usuário.")
