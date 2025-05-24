

print("-"*30)
print("Validador de Nota e Frequência")
print("-"*30)

try:
    nota = float(input("Digite a nota do aluno: ").replace(",", "."))
    #freq = int(freq_aluno)
   # dias_uteis = int(input("Digite o número total de dias úteis: "))
    dias_uteis = 253
    dias_presente = int(input("Digite o número de dias que o aluno esteve presente: "))

    freq = round((dias_presente / dias_uteis) * 100, 2)
    print("Frequência calculada:", freq,"%")
    print("-"*30)
    print("Nota informada: ",nota)
    print("Frequência:", freq,"%")


    if nota >= 7 and freq >= 75:
        print("-"*30)
        print("Aprovado!")
    else:
        print("-"*30)
        print("Reprovado!")    

except: 
    print("Erro: Por favor, digite um número.")

input("Pressione qualquer tecla para sair...")