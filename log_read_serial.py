import serial
import datetime

# Configurações da porta serial
porta_serial = '/dev/ttymxc0'  # Substitua pela porta serial correta
baud_rate = 115200
arquivo_log = "log_serial.txt"  # Nome do arquivo onde as mensagens serão salvas

try:
    # Abre a porta serial
    with serial.Serial(porta_serial, baud_rate, timeout=1) as ser, open(arquivo_log, "a") as log_file:
        print("Aguardando dados na porta serial...")

        # Loop para leitura contínua
        while True:
            # Lê a resposta da serial
            resposta = ser.readline().decode('utf-8').strip()
            if resposta:  # Verifica se há dados recebidos
                # Registra a data e hora da mensagem
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                mensagem_log = f"{timestamp} - {resposta}\n"

                # Exibe a mensagem no terminal
                print("Resposta recebida:", resposta)

                # Salva a mensagem no arquivo
                log_file.write(mensagem_log)
                log_file.flush()  # Garante que os dados sejam gravados imediatamente

except serial.SerialException as e:
    print(f"Erro de comunicação serial: {e}")
except KeyboardInterrupt:
    print("Leitura serial interrompida pelo usuário.")
