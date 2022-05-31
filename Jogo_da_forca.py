#Matheus Góes Santos Rocha - Engenharia de Software 2022/1


def sortear_palavra():
    import random
    arq = open("br-sem-acentos.txt")
    linhas = arq.readlines()
    palavra = ''
    while len(palavra) < 4:
        sorteio = random.randint(0, len(linhas)) + 1
        palavra = linhas[sorteio]
    arq.close()
    return palavra.upper().strip()


def desenhar_forca():

    forca = ''

    green_head = '\033[1;32m O \033[m'
    green_left_arm = '\033[1;32m/\033[m'
    green_rigth_arm = '\033[1;32m\ \033[m'
    green_rigth_leg = '\033[1;32m\ \033[m'
    green_left_leg = '\033[1;32m/\033[m'
    green_body = '\033[1;32m|\033[m'

    red_head = '\033[1;31m O \033[m'
    red_left_arm = '\033[1;31m/\033[m'
    red_rigth_arm = '\033[1;31m\ \033[m'
    red_rigth_leg = '\033[1;31m\ \033[m'
    red_left_leg = '\033[1;31m/\033[m'
    red_body = '\033[1;31m|\033[m'

    if erros == 0:
        forca = f'''
        .______.
        |      |
        |     {green_head}
        |     {green_left_arm}{green_body}{green_rigth_arm}
        |      {green_body}
        |     {green_left_leg} {green_rigth_leg}
        I'''
    else:
        if erros == 1:
           forca = f''' 
            .______.
            |      |
            |     {green_head}
            |     {green_left_arm}{green_body}{green_rigth_arm}
            |      {green_body}
            |     {green_left_leg} {red_rigth_leg}
            I'''
        else:
            if erros == 2:
                forca = f'''
                .______.
                |      |
                |     {green_head}
                |     {green_left_arm}{green_body}{green_rigth_arm}
                |      {green_body}
                |     {red_left_leg} {red_rigth_leg}
                I'''
            else:
                if erros == 3:
                    forca = f'''
                    .______.
                    |      |
                    |     {green_head}
                    |     {green_left_arm}{red_body}{green_rigth_arm}
                    |      {red_body}
                    |     {red_left_leg} {red_rigth_leg}
                    I'''
                else:
                    if erros == 4:
                        forca = f'''
                        .______.
                        |      |
                        |     {green_head}
                        |     {green_left_arm}{red_body}{red_rigth_arm}
                        |      {red_body}
                        |     {red_left_leg} {red_rigth_leg}
                        I'''
                    else:
                        if erros == 5:
                            forca = f''''
                            .______.
                            |      |
                            |     {green_head}
                            |     {red_left_arm}{red_body}{red_rigth_arm}
                            |      {red_body}
                            |     {red_left_leg} {red_rigth_leg}
                            I'''

    return forca

palavra = sortear_palavra()
letras_certas = ''
letras_erradas = ''
acertos = 0
erros = 0


while acertos != len(palavra) and erros != 6:
    resposta = ''
    for letra in palavra:
        if letra in letras_certas:
            resposta += letra
        else:
            resposta += '_ '
    print(f'{desenhar_forca()}')
    print(f'           {resposta} ')

    letra = input('Digite uma letra: ').upper()

    if letras_erradas != '':
        print('Você ja errou: ' + letras_erradas)

    if letra in letras_certas + letras_erradas:
        print('Você já tentou essa letra.')

    else:
        if letra in palavra:
            print('acertou')
            letras_certas += letra
            acertos += palavra.count(letra)

        else:
            print('errou')
            letras_erradas += letra
            erros += 1

if erros == 6:
    print('\033[1;31m-_'*15)
    print('VOCÊ PERDEU =(')
    print(f'A palavra era:\033[1;94m {palavra}\033[m')
    print('\033[1;31m-_\033[m' * 15)
else:
    if acertos == len(palavra):
        print('\033[1;32m-_' * 15)
        print('Você ganhou!!!')
        print('\033[1;32m-_\033[m' * 15)

print('Fim de jogo.')