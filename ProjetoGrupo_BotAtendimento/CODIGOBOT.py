#DEFININDO COMANDOS

menu1_print = "1 - Consultas \n2 - Transferir para o atendente \n3 - Informações sobre planos de saúde \n4 - Promoções  e pacotes \n5 - Outros\n"
menu2_print = "6 - Cancelamento de consultas \n7 - Banco de vagas \n8 - Reclamações \n9 - Voltar\n"

#FUNÇÕES DO MENU

def menu1(prob) :
    if prob == 1 :
        localizacao = input("Por gentileza, informe o estado e a cidade que você reside: ").upper()
        print("O link para agendar consultas em", localizacao, "é www.clinicax.com/agendamentos\n")
        print("Você deseja voltar ao menu principal ou encerrar o atendimento? \nPara encerrar o atendimento, digite ENCERRAR \nPara voltar, digite VOLTAR\n")
        retornar = input().upper()
        if len (retornar) == "ENCERRAR":
                print("A clínica X agradece o seu contato e lhe deseja um ótimo dia!")
        elif retornar == "VOLTAR":
            print(menu1_print)
            prob = int(input())
            menu1(prob)
    elif prob == 2 :
        print("Tudo bem!")
        print("Por favor, aguarde enquanto lhe transferimos para um consultor.")
        print("O tempo de espera é de até 15 minutos.\n")
        print("Você deseja voltar ao menu principal ou aguardar o atendimento? \nPara aguardar o atendimento, digite AGUARDAR \nPara voltar, digite VOLTAR\n")
        retornar = input().upper()
        if retornar == "AGUARDAR":
            print("Por favor, aguarde mais um momento.")
        elif retornar == "VOLTAR":
            print(menu1_print)
            prob = int(input())
            menu1(prob)
    elif prob == 3 :
        print("No momento, temos convênio apenas com os seguintes planos: \nPlano Azul \nEstrela Seguradora \nPreviMed")
        print("Caso você se encaixe, você pode agendar consultas pelo link abaixo: \n www.clinicax.com/agendamentoplano\n")
        print("Você deseja voltar ao menu principal ou encerrar o atendimento? \nPara encerrar o atendimento, digite ENCERRAR \nPara voltar, digite VOLTAR\n")
        retornar = input().upper()
        if retornar == "ENCERRAR":
            print("A clínica X agradece o seu contato e lhe deseja um ótimo dia!")
        elif retornar == "VOLTAR":
            print(menu1_print)
            prob = int(input())
            menu1(prob)
    elif prob == 4 :
        print("Que bom que você está interessado em cuidar da sua saúde! A clínica X está aqui para te apoiar em cada passo dessa jornada.")
        print("Vou te mandar os nosso pacotes no momento!")
        print("Pacote Nutrição \n5 consultas de R$800,00 por R$450,00 \nCondições: As consultas podem ser agendadas dentro dos próximos 12 meses, e só podem ser agendadas pelo mesmo CPF de quem realizou a compra.")
        print("Pacote Nutrição + Endocrinologista \n 2 consultas de R$400,00 por R$299,99 \nCondições: As consultas podem ser agendadas dentro dos próximos 2 meses, e só podem ser agendadas pelo mesmo CPF de quem realizou a compra")
        print("Pacote Fonoaudiologia \n 12 consultas de R$1200,00 por R$750,00 \nCondições: As consultas podem ser agendadas dentro dos próximos 6 meses, e só podem ser agendadas pelo mesmo CPF de quem realizou a compra")
        print("Você pode realizar a compra dos pacotes pelo link abaixo: \nwww.clinicax.com/pacotesepromos\n")
        print("Você deseja voltar ao menu principal ou encerrar o atendimento? \nPara encerrar o atendimento, digite ENCERRAR \nPara voltar, digite VOLTAR\n")
        retornar = input().upper()
        if retornar == "ENCERRAR":
            print("A clínica X agradece o seu contato e lhe deseja um ótimo dia!")
        elif retornar == "VOLTAR":
            print(menu1_print)
            prob = int(input())
            menu1(prob)
    else :
        print(menu2_print)
        prob2 = int(input("Insira a opção:"))
        menu2(prob2)

def menu2(prob2) :
    if prob2 == 6 :
        print("Estamos puxando as suas informações, só um momento...")
        consulta_canc = input("Por favor, informe o dia e o horário da sua consulta:")
        print("Muito obrigada,", nome_atendimento, ". Vamos cancelar a sua consulta.")
        print("Um e-mail de confirmação será encaminhado para você em até 24h úteis.")
        print("Caso haja direito a algum reembolso, será depositado em até 72h úteis na mesma conta que foi realizado o pagamento.")
        print("Para mais informações, confira o regulamento pelo link abaixo: \nwww.clinicax.com/regulamento\n")
        print("Você deseja voltar ao menu principal ou encerrar o atendimento? \nPara encerrar o atendimento, digite ENCERRAR \nPara voltar, digite VOLTAR\n")
        retornar = input().upper()
        if retornar == "ENCERRAR":
            print("A clínica X agradece o seu contato e lhe deseja um ótimo dia!")
        elif retornar == "VOLTAR":
            print(menu1_print)
            prob = int(input())
            menu1(prob)
    elif prob2 == 7 :
        print("Infelizmente, no momento, não há vagas disponíveis no banco de vagas. Por gentileza, envie seu currículo no nosso e-mail recrutamentorh@clinicax.com.br ")
        print("Caso surja uma vaga que se encaixa no seu perfil, lhe chamaremos para uma entrevista\n")
        print("Você deseja voltar ao menu principal ou encerrar o atendimento? \nPara encerrar o atendimento, digite ENCERRAR \nPara voltar, digite VOLTAR\n")
        retornar = input().upper()
        if retornar == "ENCERRAR":
            print("A clínica X agradece o seu contato e lhe deseja um ótimo dia!")
        elif retornar == "VOLTAR":
            print(menu1_print)
            prob = int(input())
            menu1(prob)
    elif prob2 == 8 :
        print("Sentimos muito por não conseguirmos atingir as suas expectativas!")
        print("Vamos fazer o seguinte: Você me conta o problema enquanto eu lhe transfiro para um consultor que irá resolver a situação para você, tudo bem?")
        reclamacao = input("Nos informe a sua situação e como podemos lhe ajudar. \n")
        print("Sentimos muito por isso. Por favor, aguarde apenas um momento. A previsão de resposta é de até 15 minutos.\n")
        print("Você deseja voltar ao menu principal ou encerrar o atendimento? \nPara encerrar o atendimento, digite ENCERRAR \nPara voltar, digite VOLTAR\n")
        retornar = input().upper()
        if retornar == "ENCERRAR":
            print("A clínica X agradece o seu contato e lhe deseja um ótimo dia!")
        elif retornar == "VOLTAR":
            print(menu1_print)
            prob = int(input())
            menu1(prob)
    else : 
        print(menu1_print)
        prob = int(input())
        menu1(prob)
        
#APRESENTAÇÃO

print("Olá! Que bom te ver por aqui.")
print("Eu me chamo Lola, sou sua assistente virtual")
nome_atendimento = input("Com quem eu falo? ")
print("Prazer,", nome_atendimento, "! Seja bem-vindo a clínica X. \n")

# COLETANDO OS DADOS DO CLIENTE

print("Antes de iniciarmos o atendimento, vamos fazer o seu cadastro, tudo bem? ")
print("Não levará mais do que 2 minutos!\n")
nome_cliente = input("Informe seu nome completo: ")
cpf_cliente = input("Informe seu CPF: ")
data_nasc_cliente = input("Informe a sua data de nascimento: ")
email_cliente = input("Informe seu e-mail de contato: \n")

print("Como podemos lhe ajudar?")
print(menu1_print)
prob = int(input("Digite a opção escolhida: \n"))
menu1(prob)
