import os  # Biblioteca para manipulação de arquivos e diretórios
import pyaes  # Biblioteca para criptografia/descriptografia AES

# Nome do arquivo criptografado que será descriptografado
file_name = "teste.txt.ransomwaretroll"

try:
    # Abrir o arquivo criptografado em modo de leitura binária
    with open(file_name, "rb") as file:
        file_data = file.read()  # Ler os dados do arquivo criptografado
    
    # Chave utilizada para a descriptografia (deve ser idêntica à usada na criptografia)
    key = b"testeransomwares"  # A chave deve ter exatamente 16, 24 ou 32 bytes
    
    # Inicializar o modo de operação AES no modo CTR (Counter Mode)
    aes = pyaes.AESModeOfOperationCTR(key)
    
    # Descriptografar os dados do arquivo
    decrypt_data = aes.decrypt(file_data)
    
    # Remover o arquivo criptografado após a leitura
    os.remove(file_name)
    
    # Criar um novo arquivo com os dados descriptografados
    new_file_name = "teste.txt"  # Nome do arquivo original restaurado
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)
    
    print(f"Arquivo '{file_name}' descriptografado com sucesso para '{new_file_name}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
