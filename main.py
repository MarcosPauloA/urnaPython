print("Bem Vindo A Urna Eletrônica!");

# Função responsável por mostrar comandos disponíveis para usuário
def mostraComandos():
    print("1 - Ler arquivo de candidatos");
    print("2 - Ler arquivo de eleitores");
    print("3 - Iniciar votação");
    print("4 - Apurar resultados");
    print("5 - Mostrar resultados");
    print("6 - Fechar programa");

# Variáveis e função responsáveis por verificar se os arquivos foram carregados antes de realizar os comandos 3, 4 ou 5
candidatosCarregados = False;
eleitoresCarregados = False;
def verificaSeArquivosForamCarregados():
    if (candidatosCarregados and eleitoresCarregados):
        return True;
    else:
        print("Arquivos precisam ser carregados antes de realizar essa ação!");
        return False;
'''
def encontraEleitor(cpfEleitor):
    i = 0;
    for eleitor in listaEleitores:
        print(listaEleitores[0][2]);
        print(cpfEleitor);
        if listaEleitores[i][2] == cpfEleitor:
           print(eleitor);
        else:
            i += 1;
'''
# Inicializando variáveis do programa
listaCandidatos = [];  
listaEleitores = [];
estadoUrna = "";    
comando = 0;
while comando != 6:
    mostraComandos();
    comando = int(input("Por favor digite o comando desejado: "));
    if comando == 1:
        nomeArquivoCandidatos = input("Informe a localização dos dados dos candidatos: ");
        try:
            file = open(nomeArquivoCandidatos);
            linha = file.readline();
            while linha:
                listaCandidatos.append(linha.split(','));
                linha = file.readline();

            candidatosCarregados = True;
            print("Arquivo carregado com sucesso!")
        except:
            print("Arquivo Não Localizado!")
        
        
    if comando == 2:
        nomeArquivoEleitores = input("Informe a localização dos dados dos eleitores: ");
        try :
            file = open(nomeArquivoEleitores);
            linha = file.readline();
            while linha:
                listaEleitores.append(linha.split(','));
                linha = file.readline();
                
            eleitoresCarregados = True;
            print("Arquivo carregado com sucesso!")
        except:
            print("Arquivo Não Localizado!")
        
    if comando == 3:
        if verificaSeArquivosForamCarregados():
            if estadoUrna == "":
                estadoUrna = input("UF onde está localizada a urna: ");
            cpfEleitor = input("Informe o Título de Eleitor: ");
            # o nome e o estado desse eleitor deverão ser mostrados na tela. 
            #encontraEleitor(cpfEleitor);
    if comando == 4:
        if verificaSeArquivosForamCarregados():
            print("Apurar votos");
    if comando == 5:
        if verificaSeArquivosForamCarregados():
            print("Mostrar resultados");
        