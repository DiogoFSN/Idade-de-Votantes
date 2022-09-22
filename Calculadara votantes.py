

voters = []

while True:
    number_voters = input('Digite o número de votantes presentes: ')
    if not number_voters.isnumeric():
        print('Digite somente número inteiros.')
    else:
        number_voters = int(number_voters)

    i = 1    
    while (number_voters) >= i:
        age_voters = input(f'Digite a idade do Votate {i}: ')
        if not age_voters.isnumeric():
            print('Digite somente número inteiros.')
        else:
            age_voters = int(age_voters)
            if age_voters < 16:
                print('Menores de 16 anos não podem votar.')
            else:
                i += 1
                voters.append(age_voters)

    print(f'Essa é a idade dos votantes presentes {voters}.')

    make_average = input('Deseja realizar a média de idade dos votantes? [s]im [n]ão: ')
    if make_average == 's':
        soma = sum(voters)
        media = soma/number_voters
        print(f'Essa é a média de idade dos votantes presentes {media}')

    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break


        