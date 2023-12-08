# Biblioteca responsável pela persistência de dados dos votos
import pickle

# Biblioteca responsável pela geração de gráficos
import matplotlib.pyplot as plt

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


# Função responsável por encontrar eleitor com determinado CPF/Título e retorna True/False caso encontrado ou não
def encontraEleitor(cpfEleitor):
    for eleitor in listaEleitores:
        if eleitor[2] == cpfEleitor and eleitor[4] == estadoUrna:
            print("Eleitor: ", eleitor[0]);
            print("Estado: ", eleitor[4]);
            eleitoresQueVotaram.append(eleitor);
            return True;
 
    print("Título Não Encontrado!");
    return False;


# Função responstável por confirmar o voto
def confirmaVoto(voto):
    confirma = input("Confirma (S ou N)? ");
    if confirma == "S":
        listaVotos.append(voto);
        return True;
    else:
        return False;


# Função responsável pelo voto a determinado candidato
def votaCandidato(numeroVoto, codigoCargo):
    estadoEleitor = eleitoresQueVotaram[len(eleitoresQueVotaram)-1][4];
    
    for candidato in listaCandidatos:
        if codigoCargo == "P":
            if numeroVoto == candidato[1] and codigoCargo == candidato[4]:
                print("Candidato ", candidato[0], " | ", candidato[2]);
                voto = numeroVoto;
                return confirmaVoto(voto);

        else:
            if numeroVoto == candidato[1] and estadoEleitor == candidato[3] and codigoCargo == candidato[4] :
                print("Candidato ", candidato[0], " | ", candidato[2]);
                voto = numeroVoto;
                return confirmaVoto(voto);

    if numeroVoto == "B":
        print("Voto em Branco");
        voto = "B";
        return confirmaVoto(voto);

    else:
        print("Candidato não encontrado! Voto Nulo.")
        voto = "N";
        return confirmaVoto(voto);
    

# Função responsável por receber do usuário se ele deseja ou não realizar outro voto e retornar true ou false
def desejaRealizarNovoVoto():
    print("--------------------------------");
    resposta = input("Registrar novo voto (S ou N)? \n")
    print("--------------------------------");
    if resposta == "S":
        return True;
    elif resposta == "N":
        return False;
    else:
        print("Comando Inválido!");
        return desejaRealizarNovoVoto();


# Função responsável por encontrar determinado candidato e retorna-lo
def encontraCandidato(numeroCandidato, codigoCargo, estado):
    for candidato in listaCandidatos:
        if codigoCargo == "P":
            if numeroCandidato == candidato[1] and codigoCargo == candidato[4]:
                return candidato;

        else:
            if numeroCandidato == candidato[1] and estado == candidato[3] and codigoCargo == candidato[4] :
                return candidato;


# Função responsável por verificar se o candidato alvo está ou não no dicionário
def verificaSeTemNoDicionario(listaDicionario, candidato):
    for dicionario in listaDicionario:
        if dicionario['candidato'] == candidato:
            return True;
    return False;


def escreveBoletimUrna(totalVotos, votosNominais, votosBrancos, votosNulos, listaDicionariosVotos):
    arq = open("boletimDeUrna", 'w', encoding="utf-8");
    arq.write("Eleitores aptos: %d\n" %(totalVotos));
    arq.write("Total de Votos Nominais: %d\n" %(votosNominais));
    arq.write("Brancos: %d\n" %(votosBrancos));
    arq.write("Nulos: %d\n\n" %(votosNulos));
    for dicionario in listaDicionariosVotos:
        dicionarioApurado.append({dicionario['candidato']: dicionario['votos']});
        arq.write(f"Candidato: {dicionario['candidato']} | Cargo: {dicionario['cargo']} | Estado: {dicionario['estado']} | Votos: {dicionario['votos']} ({(dicionario['votos']/totalVotos)*100}%)\n");
    arq.close();


def gera_grafico(titulo, votos):
    candidatos = [];
    numeroVotos = [];
    for item in votos:
        for candidato, numeroVoto in item.items():
            candidatos.append(candidato);
            numeroVotos.append(numeroVoto);
    
    # Criando o gráfico de barras
    plt.bar(candidatos, numeroVotos,  color="#6c3376")

    # Configuração de layout
    plt.ylabel('Votos')
    plt.xlabel('Candidatos')
    plt.title(titulo)

    # Imprimindo o gráfico
    plt.show()


# Inicializando variáveis do programa
listaVotos = [];
listaDicVotos = [];
listaCandidatos = [];  
listaEleitores = [];
estadoUrna = ""; 
eleitoresQueVotaram = []; 
dicionarioApurado = [];  
# Dicionário que mapeia os cargos aos seus respectivos códigosLetra
cargos = {"Deputado Federal": "F", "Deputado Estadual": "E", "Senador": "S", "Governador": "G", "Presidente": "P"}
comando = 0;
while comando != 6:
    mostraComandos();
    comando = int(input("Por favor digite o comando desejado: "));
    # 1 Para comando de ler arquivo de candidatos
    if comando == 1:
        nomeArquivoCandidatos = input("Informe a localização dos dados dos candidatos: ");
        try:
            arq = open(nomeArquivoCandidatos, "r", encoding="utf-8");
            linha = arq.readline();
            while linha:
                linhaSemVirgulas = linha.split(', ');
                listaCandidatos.append(linhaSemVirgulas);
                # Na linha abaixo removendo o \n do último elemento
                listaCandidatos[len(listaCandidatos)-1][4] = listaCandidatos[len(listaCandidatos)-1][4].replace("\n", "")
                linha = arq.readline();
            candidatosCarregados = True;
            print("Arquivo carregado com sucesso!");
            arq.close();
        except:
            print("Arquivo Não Localizado!")
        
    # 2 Para comando de ler arquivo de eleitores
    elif comando == 2:
        nomeArquivoEleitores = input("Informe a localização dos dados dos eleitores: ");
        try :
            arq = open(nomeArquivoEleitores, "r", encoding="utf-8");
            linha = arq.readline();
            while linha:
                linhaSemVirgulas = linha.split(', ');
                listaEleitores.append(linhaSemVirgulas);
                # Na linha abaixo removendo o \n do último elemento
                listaEleitores[len(listaEleitores)-1][4] = listaEleitores[len(listaEleitores)-1][4].replace("\n", "")
                linha = arq.readline();
            eleitoresCarregados = True;
            print("Arquivo carregado com sucesso!");
            arq.close();
        except:
            print("Arquivo Não Localizado!")
    
    # 3 Para comando de iniciar votação    
    elif comando == 3:
        if verificaSeArquivosForamCarregados():
            if estadoUrna == "":
                estadoUrna = input("UF onde está localizada a urna: ");
            novoVoto = True;
            while novoVoto:
                cpfEleitor = input("Informe o Título de Eleitor: ");
                if (encontraEleitor(cpfEleitor)):
                    # Agora que o eleitor foi encontrado itera pelo dicionário de cargos e recebe os votos para cada cargo 
                    for cargo, codigoCargo in cargos.items():
                        numeroVoto = input(f"Informe o voto para {cargo}: ");
                        while(not votaCandidato(numeroVoto, codigoCargo)):
                            numeroVoto = input(f"Informe o voto para {cargo}: ");
                            
                    # Criando o dicionário do voto que será armazenado em um arquivo binário
                    voto = {"UF": estadoUrna, "F": listaVotos[0], "E": listaVotos[1], "S": listaVotos[2], "G": listaVotos[3], "P": listaVotos[4]};
                    listaDicVotos.append(voto);
                    listaVotos = [];
                    # Registrando o voto inteiro em um arquivo binário nas 2 linhas abaixo
                    with open('votosBinario.bin', 'wb') as arquivo:
                        pickle.dump(listaDicVotos, arquivo);
                    print("\nVoto registrado com sucesso!\n")
                    
                    # Agora verificando se haverá outro voto
                    novoVoto = desejaRealizarNovoVoto();
                    

    # 4 Para comando de apurar votos
    elif comando == 4:
        if verificaSeArquivosForamCarregados():
            totalVotos = 0;
            votosNominais = 0;
            votosBrancos = 0;
            votosNulos = 0;
            listaDicionariosVotos = [];
            arquivoBinario = open('votosBinario.bin', 'rb');
            listaDicVotos = pickle.load(arquivoBinario);
            for voto in listaDicVotos:
                estado = voto['UF'];
                totalVotos += 1;
                for cargo, codigoCargo in cargos.items():
                    if voto[codigoCargo] == 'B':
                        votosBrancos += 1;
                    elif voto[codigoCargo] == 'N':
                        votosNulos += 1;
                    else:
                        candidato = encontraCandidato(voto[codigoCargo], codigoCargo, estado);
                        votosNominais += 1;
                        if verificaSeTemNoDicionario(listaDicionariosVotos, candidato[0]):
                            for dicionario in listaDicionariosVotos:
                                if dicionario['candidato'] == candidato[0]:
                                    dicionario['votos'] += 1;
                        else:
                            listaDicionariosVotos.append({'candidato': candidato[0], 'cargo': cargo, 'estado': candidato[3], 'votos': 1});            

                
            escreveBoletimUrna(totalVotos, votosNominais, votosBrancos, votosNulos, listaDicionariosVotos);
            arquivoBinario.close();
            
    # 5 Para comando de mostrar resultados       
    elif comando == 5:
        if verificaSeArquivosForamCarregados():
            gera_grafico("Apuração - Eleições", dicionarioApurado);
   
    elif comando != 6:
        print("Comando Inválido!");
    
print("Fechando Programa...");