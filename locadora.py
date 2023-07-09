# cliente
nomecliente = []
idadecliente = []
# automovel
placacarro = []
modelocarro = []
anocarro = []
carrosdisponiveis = []
# carroalugado
carroalugado = []


def cadastrocli(nomecli, idadecli):
    ncli = input('nome do cliente: ')
    if ncli in nomecliente:
        print('Cliente já cadastrado. Tente com outro sobre-nome')


    else:
        icli = input('idade do cliente: ')
        nomecliente.append(ncli)
        idadecliente.append(icli)
        print('cliente ', ncli , 'cadastrado com sucesso!')

    import time

    time.sleep(4)

def menu(escolha):
    print('[1] CADASTRO USUÁRIO')
    print('[2] CADASTRO VEICULO')
    print('[3] EXCLUIR USUÁRIO')
    print('[4] EXCLUIR VEÍCULO')
    print('[5] LOCAR / DEVOLVER VEICULO')
    print('[6] USUÁRIOS CADASTRADOS')
    print('[7] CARROS CADASTRADOS')
    print('[8] VEÍCULOS ALUGADOS NO MOMENTO')
    print('[9] VEÍCULOS DISPONIVEIS')
    escolha = int(input('O que deseja fazer? '))
    return (escolha)


def cadascar(placacarro, modelocarro, anocarro):
    pcar = input('placa do veículo: ')
    if pcar in placacarro:
        print('placa ja cadastrada. Verifique a placa do veículo')
    else:
        mcar = input('modelo do veículo [marca - nome]: ')
        acar = input('ano do veículo: ')
        placacarro.append(pcar)
        modelocarro.append(mcar)
        anocarro.append(acar)
        print('veículo :', mcar, ', ', pcar, 'adicionado com sucesso!')
        carrosdisponiveis.append(pcar)

    import time

    time.sleep(4)


def listacli(nomecli, idadecli):
    for i in range(len(nomecli)):
        ncli = nomecli[i]
        icli = idadecli
        print('/n SClientes cadastrados: {}, idade: {}'.format(ncli, icli))

    import time

    time.sleep(4)


def listacar(placacarro, modelocarro, anocarro):
    for i in range(len(modelocarro)):
        pcar = placacarro[i]
        mcar = modelocarro[i]
        acar = anocarro[i]
        print(' veículo placa: {}, modelo: {}, ano: {}'.format(pcar, mcar, acar))
    import time

    time.sleep(4)


def carroalugar():

    print('digite [1] para alugar e digite [2] para devolver')
    aluoudevol = int(input('vai alugar ou devolver o carro? '))
    if aluoudevol == 1:
        print('coloque o nome do cliente como está no cadastro')
        usuarioaluga = input('nome do cliente que vai alugar o veículo')
        if usuarioaluga in nomecliente:
            print('vamos escolher o carro agora')

            print('carros dipoiveis: ')

            print(carrosdisponiveis)

            diasalugar = input('Por quantos dias vai alugar o carro: ')
            palugar = input('qual a placa do carro vai alugar: ')
            malugar = input('modelo do carro que vai alugar: ')
            #dados = palugar + malugar + usuarioaluga

            #print(carrosdisponiveis)

            carrosdisponiveis.remove(palugar)
            if palugar in placacarro:
                dados = (palugar)
                carroalugado.append(dados)
                carroalugado.append(' cliente: ')
                carroalugado.append(usuarioaluga)

                print('O carro placa: ', palugar, 'será alugado por ', diasalugar, 'dias, pelo cliente: ', usuarioaluga)
                print(carroalugado)
                #return dados
            else:
                print('Veículo não encontrado. Verifique a placa')

        else:
            print('cliente não encontrado, confira a lista e verifique se o nome foi digitado corretamente')

    elif aluoudevol == 2:
        devolucao = input('placa do carro que vai devolver: ')
        if devolucao in carroalugado:
            clientedevolve = input('qual o nome do cliente que vai devolver o veículo: ')
            if clientedevolve in nomecliente:
                carrosdisponiveis.append(devolucao)
                carroalugado.remove(devolucao)
                carroalugado.remove(' cliente: ')
                carroalugado.remove(clientedevolve)
                print('carro: ', devolucao, ' devolvido com sucesso! ')
            else:
                print('cliente não encontrado na listad de cadastro!')
        else:
            print('O carro não está alugado!')


    import time

    time.sleep(4)

def carrolivre(carrosdisponiveis):
    print(carrosdisponiveis)
    import time

    time.sleep(4)


def excluircar():


    print(placacarro)
    print(modelocarro)
    print(anocarro)
    excluirp = input('qual carro quer excluir? informe a placa: ')
    if excluirp in placacarro:
        excluirm = input('modelo que você quer excluir: ')
        excluira = input('ano do carro que deseja excluir: ')
        placacarro.remove(excluirp)
        modelocarro.remove(excluirm)
        anocarro.remove(excluira)
        if excluirp in carrosdisponiveis:
            carrosdisponiveis.remove(excluirp)
        print('carro placa: ', excluirp, ' modelo: ', excluirm, ' ano:', excluira, ' excluído com sucesso!')
    else:
        print('carro não encontrado. Verifique a placa do veículo!')

    import time


    time.sleep(4)


def excluircli(nomecliente, idadecliente):
    print(nomecliente)
    print(idadecliente)
    excluirn = input('nome do usuario a ser excluido: ')
    if excluirn in nomecliente:
        excluiri = input('idade do usuário no dia do cadastro: ')
        nomecliente.remove(excluirn)
        idadecliente.remove(excluiri)
        print('cliente: ', excluirn, ' excluído!')
    else:
        print('cliente não encontrado')
    import time

    time.sleep(4)


def listarcli(nomecliente, idadecliente):
    for i in range(len(nomecliente)):
        ncli = nomecliente[i]
        icli = idadecliente[i]
        print(' nome do cliente: {}, idade: {}'.format(ncli, icli))

    import time

    time.sleep(4)


def acao():
    escolha = 9

    while escolha != 0:
        escolha = menu(escolha)


        if escolha == 1:
            print('Vamos cadastrar o usuário!')
            cadastrocli(nomecliente, idadecliente)

        elif escolha == 2:
            print('vamos cadastrar o veículo!')
            cadascar(placacarro, modelocarro, anocarro)
        elif escolha == 3:
            print('excluir usuário')
            excluircli(nomecliente, idadecliente)
        elif escolha == 4:
            print('excluir veículo')
            excluircar()
        elif escolha == 5:
            print('locar ou devolver veiculo!')
            carroalugar()
        elif escolha == 6:
            print('esses são os usuários cadastrados:')
            listarcli(nomecliente, idadecliente)
        elif escolha == 7:
            print('esses são todos os carros cadastrados: ')
            listacar(placacarro, modelocarro, anocarro)
        elif escolha == 8:
            print('esses são os carros alugados no momento: ')
            print(carroalugado)
            import time
            time.sleep(4)
        elif escolha == 9:
            print('esses são os carros disponíveis:')
            carrolivre(carrosdisponiveis)
        else:
            print('opção invalida digite novamente')
            import time

            time.sleep(4)


acao()