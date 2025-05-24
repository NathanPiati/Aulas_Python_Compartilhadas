from datetime import date


ano_atual = date.today().year
entrada = input("Digite o seu ano de nascimento no formato dd/mm/aaaa: ")
dia, mes, ano_nasc = map(int, entrada.split('/'))
idade = ano_atual - ano_nasc

print(entrada)

if idade >= 18:
    print("Você pode entrar na festa!")
    print("Beba sem moderação!")
else:
    print("Você não pode entrar na festa, você tem", idade, "anos de idade.")
    print("Ligue para sua mãe e volte para a casa!")

