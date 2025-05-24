from datetime import date

ano_atual = date.today().year
mes_atual = date.today().month
dia_atual = date.today().day
entrada = input("Digite o seu ano de nascimento no formato dd/mm/aaaa: ")
dia, mes, ano_nasc = map(int, entrada.split('/'))
idade = ano_atual - ano_nasc

if mes_atual < mes or (mes_atual == mes and dia_atual < dia):
    idade -= 1

print(ano_atual)
print(mes_atual)
print(dia_atual)

if idade <= 12:
    print("A data digitada é:", entrada)
    print("Você se enquadra no grupo CRIANÇA!")
    print("Possui", idade, "anos de idade.")

elif 13 <= idade <= 17:
    print("A data digitada é:", entrada)
    print("Você se enquadra no grupo ADOLESCENTE!")
    print("Possui", idade, "anos de idade.")

elif 18 <= idade <= 59:   
    print("A data digitada é:", entrada)
    print("Você se enquadra no grupo ADULTO!")
    print("Possui", idade, "anos de idade.")

elif idade >= 60:
    print("A data digitada é:", entrada)
    print("Você se enquadra no grupo IDOSO!")
    print("Possui", idade, "anos de idade.")    
    
else:
    print("Você não pode entrar na festa, você tem", idade, "anos de idade.")
    print("Ligue para sua mãe e volte para a casa!")

input("Pressione qualquer tecla para sair...")
