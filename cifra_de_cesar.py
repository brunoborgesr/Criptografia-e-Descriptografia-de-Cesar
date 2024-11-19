import random
import itertools
from time import time
from time import sleep

print('\n-Senha aleatória entre 3 e 7 caracteres contendo apenas letras maiúsculas, letras minúsculas e números sendo criada e sendo criptografada...')
sleep(5)
caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnpqrstuvwxyz1234567890'
tamanho_senha = random.randint(3, 7)
r = random.sample(caracteres, tamanho_senha)
senha_original = ''.join(r)
deslocamento = random.randint(1, 61)
senha_criptografada = ''

for algarismo in senha_original:
    if algarismo in caracteres:
        posicao_original = caracteres.index(algarismo)
        nova_posicao = (posicao_original + deslocamento) % len(caracteres)
        senha_criptografada += caracteres[nova_posicao]

print(f'-A senha criptografada é: {senha_criptografada}')

print('-Senha sendo preparada para ser decifrada...')
sleep(5)

print('-Tudo pronto!')
sleep(2)

senha_encontrada = False
inicio_temp = time()
tentativas = 0

for comprimento in range(3, 8):
    if senha_encontrada == True:
        break
    for combinacao in itertools.product(caracteres, repeat=comprimento):
        senha_decodificada = ''.join(combinacao)
        tentativas += 1
        print(f'Tentativa {tentativas}: {senha_decodificada}')

        if senha_decodificada == senha_original:
            fim_temp = time()
            print(f'\n-Senha encontrada: {senha_decodificada}')
            print(f'-Total de tentativas: {tentativas}')
            print(f'-Tempo total: {fim_temp - inicio_temp:.2f} segundos')
            senha_encontrada = True
            break