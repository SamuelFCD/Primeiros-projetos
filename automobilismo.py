import csv

def ler_csv(arquivo):

    dados = []

    try:

        with open(arquivo, mode='r', encoding='utf-8') as arquivo_csv:

            leitor_csv = csv.DictReader(arquivo_csv,delimiter=',')

            for linha in leitor_csv:

                dados.append(linha)

            return dados

    except IOError as e:

        with open(arquivo, 'w', newline='') as arquivo_csv:

            pass
def escrever_csv(dados, arquivo):

    if not dados:

        return

    cabecalhos = dados[0].keys()

    with open(arquivo, mode='w', encoding='utf-8', newline='') as arquivo_csv:

        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos,delimiter=',')

        escritor_csv.writeheader()

        for linha in dados:

            escritor_csv.writerow(linha)

def equipe():

    dados_lidos = ler_csv('equipes.csv')

    listar_equipe(dados_lidos)


def listar_equipe(equipes):

    if not equipes:

        print('Equipes da biblioteca : ')

        print('não a nem uma equipe !')

    else:

        print('Equipes da biblioteca : ')

        for equipe in equipes:

            print(equipe)

    buscar_equipe(equipes)


def buscar_equipe(equipes):

    d = input('Deseja saber se sua equipe foi adicionada a nossa lista ?').upper().strip()

    if d == 'SIM':

        busca = input('NOME DA EQUIPE ( DIGITE CORRETAMENTE ) :').upper().strip()

        buscar_equipe = []

        tem = False

        for nome_equipe in equipes:

            buscar_equipe.extend(nome_equipe.values())

        for x in buscar_equipe:

            if busca == x:

                print('Equipe encontrada : ', x)

                for indice, dicionario in enumerate(equipes):

                    if dicionario['nome'] == x:

                        valor = indice

                        info_equipes(equipes, x)

                        m = input('quer mudar algum dado da equipe ?').upper().strip()

                        if m == 'SIM':

                            alteraçao(equipes,valor)

                        else:

                            ad = input('deseja adicionar alguma equipe ? ').upper().strip()

                            if ad == 'SIM':

                                adicionar_equipe(equipes)

                            else:

                                equipe()

                tem = True

                break

            else:

                pass

        if tem == False:

            print('A equipe não foi encontrada !')

            s = input('Deseja adionar essa equipe ou alguma outra ?').strip().upper()

            if s == 'SIM':

                adicionar_equipe(equipes)

            else:

                equipe()
    else:

        e = input('deseja adicionar alguma equipe ? ').upper().strip()

        if e == 'SIM':

            adicionar_equipe(equipes)

def adicionar_equipe(equipes):

    nome = input('Qual o nome dessa equipe ? ').upper().strip()

    pilotos = input('Quais são os pilotos dessas equipes').upper().strip()

    ano = int(input('Qual o ano dessa equipe'))

    nova_equipe = {'nome':nome, 'pilotos':pilotos, 'ano':ano}

    equipes.append(nova_equipe)

    escrever_csv(equipes,'equipes.csv')

    equipe()

def info_equipes(equipes,nome):

    d = input(f'deseja ver as informações gerais sobre a equipe : {nome}').upper().strip()

    if d == 'SIM':

        for x in equipes:

            if x['nome'] == nome:

                print(x)


    else:


        adicionar_equipe(equipes)




def alteraçao(equipes,x):

    modificar = input('o que voce quer modificar/adicionar : nome , pilotos , ano ? ').upper()

    if modificar == 'NOME':

        alterar = input('Digite a alteração : ').upper()

        equipes[x]['nome'] = alterar



    if modificar == 'PILOTOS':

        alterar = input('Digite a alteração : ')

        equipes[x]['pilotos'] = alterar



    if modificar == 'ANO':

        alterar = input('Digite a alteração : ')

        equipes[x]['ano'] = alterar



    escrever_csv(equipes,'boar.csv')

    excluir(equipes , x)

    equipe()

def excluir(equipes, x):
    excluir = input('Deseja excluir alguma informação dessa equipe ?').upper().strip()
    if excluir == 'SIM':

        ex = input('o que voce quer excluir  : nome , pilotos , ano ? ').upper()

        if ex == 'NOME':

             equipes[x]['nome'] = 'SEM DADOS'

        if ex == 'PILOTOS':

            equipes[x]['pilotos'] = 'SEM DADOS'

        if ex == 'ANO':

            equipes[x]['ano'] = 'SEM DADOS'

        escrever_csv(equipes,'equipes.csv')

        equipe()





if __name__ == "__main__":


    equipe()
