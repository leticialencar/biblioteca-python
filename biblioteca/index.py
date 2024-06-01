print("BIBLIOTECA")

livro_titulo1 = "Prateleira vazia"
livro_locador1 = ""
dias_p_devolver1 = 0
dias_v1 = True

livro_titulo2 = "Prateleira vazia"
livro_locador2 = ""
dias_p_devolver2 = 0
dias_v2 = True

livro_titulo3 = "Prateleira vazia"
livro_locador3 = ""
dias_p_devolver3 = 0
dias_v3 = True

livro_titulo4 = "Prateleira vazia"
livro_locador4 = ""
dias_p_devolver4 = 0
dias_v4 = True

livro_titulo5 = "Prateleira vazia"
livro_locador5 = ""
dias_p_devolver5 = 0
dias_v5 = True


def adicionar_livro(titulo, prateleira):
    global livro_titulo1, livro_titulo2, livro_titulo3, livro_titulo4, livro_titulo5

    while True:
        if str(prateleira).isdigit() and 1 <= int(prateleira) <= 5:
            prateleira = int(prateleira)
            break
        else:
            prateleira = input("Por favor, digite um número de prateleira válido (1 a 5): ")

    if prateleira == 1:
        if livro_titulo1 == "Prateleira vazia":
            livro_titulo1 = titulo
            return f"O livro {titulo} foi adicionado à prateleira {prateleira} da biblioteca."
        else:
            while True:
                resposta = input("A prateleira 1 já está ocupada. Deseja adicionar em outra prateleira? (S/N): ").upper()
                if resposta == "S":
                    prateleira = int(input("Em qual estante você deseja adicionar? (1 a 5): "))
                    return adicionar_livro(titulo, prateleira)
                elif resposta == "N":
                    return "Operação de adicionar livro cancelada."
                else:
                    print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")
    elif prateleira == 2:
        if livro_titulo2 == "Prateleira vazia":
            livro_titulo2 = titulo
            return f"O livro {titulo} foi adicionado à prateleira {prateleira} da biblioteca."
        else:
            while True:
                resposta = input("A prateleira 2 já está ocupada. Deseja adicionar em outra prateleira? (S/N): ").upper()
                if resposta == "S":
                    prateleira = int(input("Em qual estante você deseja adicionar? (1 a 5): "))
                    return adicionar_livro(titulo, prateleira)
                elif resposta == "N":
                    return "Operação de adicionar livro cancelada."
                else:
                    print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")
    elif prateleira == 3:
        if livro_titulo3 == "Prateleira vazia":
            livro_titulo3 = titulo
            return f"O livro {titulo} foi adicionado à prateleira {prateleira} da biblioteca."
        else:
            while True:
                resposta = input("A prateleira 3 já está ocupada. Deseja adicionar em outra prateleira? (S/N): ").upper()
                if resposta == "S":
                    prateleira = int(input("Em qual estante você deseja adicionar? (1 a 5): "))
                    return adicionar_livro(titulo, prateleira)
                elif resposta == "N":
                    return "Operação de adicionar livro cancelada."
                else:
                    print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")
    elif prateleira == 4:
        if livro_titulo4 == "Prateleira vazia":
            livro_titulo4 = titulo
            return f"O livro {titulo} foi adicionado à prateleira {prateleira} da biblioteca."
        else:
            while True:
                resposta = input("A prateleira 4 já está ocupada. Deseja adicionar em outra prateleira? (S/N): ").upper()
                if resposta == "S":
                    prateleira = int(input("Em qual estante você deseja adicionar? (1 a 5): "))
                    return adicionar_livro(titulo, prateleira)
                elif resposta == "N":
                    return "Operação de adicionar livro cancelada."
                else:
                    print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")
    elif prateleira == 5:
        if livro_titulo5 == "Prateleira vazia":
            livro_titulo5 = titulo
            return f"O livro {titulo} foi adicionado à prateleira {prateleira} da biblioteca."
        else:
            while True:
                resposta = input("A prateleira 5 já está ocupada. Deseja adicionar em outra prateleira? (S/N): ").upper()
                if resposta == "S":
                    prateleira = int(input("Em qual estante você deseja adicionar? (1 a 5): "))
                    return adicionar_livro(titulo, prateleira)
                elif resposta == "N":
                    return "Operação de adicionar livro cancelada."
                else:
                    print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")

    return f"Prateleira inválida."


def aluga_livro(alugar, locador, dias):
    global livro_locador1, livro_locador2, livro_locador3, livro_locador4, livro_locador5
    global dias_p_devolver1, dias_p_devolver2, dias_p_devolver3, dias_p_devolver4, dias_p_devolver5
    global dias_v1, dias_v2, dias_v3, dias_v4, dias_v5

    while dias < 0:
        print("Por favor, insira um número de dias válido.")
        dias = int(input("Digite a quantidade de dias para locação: "))

    if alugar == livro_titulo1 and dias_v1 == True:
        livro_locador1 = locador
        dias_p_devolver1 = dias
        dias_v1 = False
        print(f"O livro {alugar}, foi alugado por {locador}, por {dias} dias.")

    elif alugar == livro_titulo2 and dias_v2 == True:
        livro_locador2 = locador
        dias_p_devolver2 = dias
        dias_v2 = False
        print(f"O livro {alugar}, foi alugado por {locador}, por {dias} dias.")

    elif alugar == livro_titulo3 and dias_v3 == True:
        livro_locador3 = locador
        dias_p_devolver3 = dias
        dias_v3 = False
        print(f"O livro {alugar}, foi alugado por {locador}, por {dias} dias.")

    elif alugar == livro_titulo4 and dias_v4 == True:
        livro_locador4 = locador
        dias_p_devolver4 = dias
        dias_v4 = False
        print(f"O livro {alugar}, foi alugado por {locador}, por {dias} dias.")

    elif alugar == livro_titulo5 and dias_v5 == True:
        livro_locador5 = locador
        dias_p_devolver5 = dias
        dias_v5 = False
        print(f"O livro {alugar}, foi alugado por {locador}, por {dias} dias.")

    else:
        print("")
        print("O livro informado já está alugado.")
        print("")
    return ""


def consulta():
    if dias_p_devolver1 == 0 and dias_v1 == True:
        print(f"\033[32m{livro_titulo1}, Está disponivel\033[m")
    else:
        print(f"\033[31m{livro_titulo1}, Foi alugado por {livro_locador1}, faltam {dias_p_devolver1 + 1} dias para devolver\033[m")
    if dias_p_devolver2 == 0 and dias_v2 == True:
        print(f"\033[32m{livro_titulo2}, Está disponivel\033[m")
    else:
        print(f"\033[31m{livro_titulo2}, Foi alugado por {livro_locador2}, faltam {dias_p_devolver2 + 1} dias para devolver\033[m")
    if dias_p_devolver3 == 0 and dias_v3 == True:
        print(f"\033[32m{livro_titulo3}, Está disponivel\033[m")
    else:
        print(f"\033[31m{livro_titulo3}, Foi alugado por {livro_locador3}, faltam {dias_p_devolver3 + 1} dias para devolver\033[m")
    if dias_p_devolver4 == 0 and dias_v4 == True:
        print(f"\033[32m{livro_titulo4}, Está disponivel\033[m")
    else:
        print(f"\033[31m{livro_titulo4}, Foi alugado por {livro_locador4}, faltam {dias_p_devolver4 + 1} dias para devolver\033[m")
    if dias_p_devolver5 == 0 and dias_v5 == True:
        print(f"\033[32m{livro_titulo5}, Está disponivel\033[m")
    else:
        print(f"\033[31m{livro_titulo5}, Foi alugado por {livro_locador5}, faltam {dias_p_devolver5 + 1} dias para devolver\033[m")
    return ""


def devolver_livro(devolver):
    global dias_p_devolver1, dias_p_devolver2, dias_p_devolver3, dias_p_devolver4, dias_p_devolver5
    global dias_v1, dias_v2, dias_v3, dias_v4, dias_v5

    if devolver == livro_titulo1:
        juros1 = juros_livro_individual(dias_p_devolver1)
        dias_p_devolver1 = 0
        dias_v1 = True
        print(f"O livro {devolver} foi devolvido.")
        print(juros1)
    elif devolver == livro_titulo2:
        juros2 = juros_livro_individual(dias_p_devolver2)
        dias_p_devolver2 = 0
        dias_v2 = True
        print(f"O livro {devolver} foi devolvido.")
        print(juros2)
    elif devolver == livro_titulo3:
        juros3 = juros_livro_individual(dias_p_devolver3)
        dias_p_devolver3 = 0
        dias_v3 = True
        print(f"O livro {devolver} foi devolvido.")
        print(juros3)
    elif devolver == livro_titulo4:
        juros4 = juros_livro_individual(dias_p_devolver4)
        dias_p_devolver4 = 0
        dias_v4 = True
        print(f"O livro {devolver} foi devolvido.")
        print(juros4)
    elif devolver == livro_titulo5:
        juros5 = juros_livro_individual(dias_p_devolver5)
        dias_p_devolver5 = 0
        dias_v5 = True
        print(f"O livro {devolver} foi devolvido.")
        print(juros5)
    else:
        print("Livro não encontrado na biblioteca.")


def juros_livro_individual(dias_p_devolver):
    juros = 0
    if dias_p_devolver < 0:
        juros = abs(dias_p_devolver) * 0.5
        return f"Devido ao atraso na devolução do livro, você terá que pagar uma taxa de {juros} R$"
    else:
        return "Livro devolvido no prazo. Não há taxa de juros a ser paga."


def realocar_livro():
    global livro_titulo1, livro_titulo2, livro_titulo3, livro_titulo4, livro_titulo5
    global dias_p_devolver1, dias_p_devolver2, dias_p_devolver3, dias_p_devolver4, dias_p_devolver5
    global dias_v1, dias_v2, dias_v3, dias_v4, dias_v5

    realocar = input("Digite o título do livro que você deseja realocar: ").strip().capitalize()

    if realocar == livro_titulo1:
        if dias_p_devolver1 < 0:
            print("Este livro está em atraso. Por favor, devolva-o antes de realocá-lo.")
            return
        while True:
            nova_devolucao = int(input("Quantos dias a mais você deseja locar o livro? "))
            if nova_devolucao >= 0:
                break
            else:
                print("Por favor, digite um número de dias válido.")
        dias_p_devolver1 += nova_devolucao
        total_dias = dias_p_devolver1 + 1

    elif realocar == livro_titulo2:
        if dias_p_devolver2 < 0:
            print("Este livro está em atraso. Por favor, devolva-o antes de realocá-lo.")
            return
        while True:
            nova_devolucao = int(input("Quantos dias a mais você deseja locar o livro? "))
            if nova_devolucao >= 0:
                break
            else:
                print("Por favor, digite um número de dias válido.")
        dias_p_devolver2 += nova_devolucao
        total_dias = dias_p_devolver2 + 1

    elif realocar == livro_titulo3:
        if dias_p_devolver3 < 0:
            print("Este livro está em atraso. Por favor, devolva-o antes de realocá-lo.")
            return
        while True:
            nova_devolucao = int(input("Quantos dias a mais você deseja locar o livro? "))
            if nova_devolucao >= 0:
                break
            else:
                print("Por favor, digite um número de dias válido.")
        dias_p_devolver3 += nova_devolucao
        total_dias = dias_p_devolver3 + 1

    elif realocar == livro_titulo4:
        if dias_p_devolver4 < 0:
            print("Este livro está em atraso. Por favor, devolva-o antes de realocá-lo.")
            return
        while True:
            nova_devolucao = int(input("Quantos dias a mais você deseja locar o livro? "))
            if nova_devolucao >= 0:
                break
            else:
                print("Por favor, digite um número de dias válido.")
        dias_p_devolver4 += nova_devolucao
        total_dias = dias_p_devolver4 + 1

    elif realocar == livro_titulo5:
        if dias_p_devolver5 < 0:
            print("Este livro está em atraso. Por favor, devolva-o antes de realocá-lo.")
            return
        while True:
            nova_devolucao = int(input("Quantos dias a mais você deseja locar o livro? "))
            if nova_devolucao >= 0:
                break
            else:
                print("Por favor, digite um número de dias válido.")
        dias_p_devolver5 += nova_devolucao
        total_dias = dias_p_devolver5 + 1
    else:
        print("Livro indisponível ou não encontrado na biblioteca.")
        return

    if not dias_v1:
        dias_p_devolver1 -= 1
    if not dias_v2:
        dias_p_devolver2 -= 1
    if not dias_v3:
        dias_p_devolver3 -= 1
    if not dias_v4:
        dias_p_devolver4 -= 1
    if not dias_v5:
        dias_p_devolver5 -= 1
        
    print("")
    print(f'O número total de dias para devolver o livro "{realocar}" foi atualizado para {total_dias} dias.')
    print("")
    

def remover_livro():
    global livro_titulo1, livro_titulo2, livro_titulo3, livro_titulo4, livro_titulo5
    global livro_locador1, livro_locador2, livro_locador3, livro_locador4, livro_locador5
    global dias_p_devolver1, dias_p_devolver2, dias_p_devolver3, dias_p_devolver4, dias_p_devolver5
    global dias_v1, dias_v2, dias_v3, dias_v4, dias_v5

    titulo_remover = (input("Digite o título do livro que você deseja remover: ").strip().capitalize())

    if titulo_remover == livro_titulo1:
        if dias_v1:
            livro_titulo1 = "Prateleira vazia"
            livro_locador1 = ""
            dias_p_devolver1 = 0
            dias_v1 = True
            print(f"O livro '{titulo_remover}' foi removido da biblioteca.")
        else:
            print("Este livro não pode ser removido no momento.")
    elif titulo_remover == livro_titulo2:
        if dias_v2:
            livro_titulo2 = "Prateleira vazia"
            livro_locador2 = ""
            dias_p_devolver2 = 0
            dias_v2 = True
            print(f"O livro '{titulo_remover}' foi removido da biblioteca.")
        else:
            print("Este livro não pode ser removido no momento.")
    elif titulo_remover == livro_titulo3:
        if dias_v3:
            livro_titulo3 = "Prateleira vazia"
            livro_locador3 = ""
            dias_p_devolver3 = 0
            dias_v3 = True
            print(f"O livro '{titulo_remover}' foi removido da biblioteca.")
        else:
            print("Este livro não pode ser removido no momento.")
    elif titulo_remover == livro_titulo4:
        if dias_v4:
            livro_titulo4 = "Prateleira vazia"
            livro_locador4 = ""
            dias_p_devolver4 = 0
            dias_v4 = True
            print(f"O livro '{titulo_remover}' foi removido da biblioteca.")
        else:
            print("Este livro não pode ser removido no momento.")
    elif titulo_remover == livro_titulo5:
        if dias_v5:
            livro_titulo5 = "Prateleira vazia"
            livro_locador5 = ""
            dias_p_devolver5 = 0
            dias_v5 = True
            print(f"O livro '{titulo_remover}' foi removido da biblioteca.")
        else:
            print("Este livro não pode ser removido no momento.")
    else:
        print("Livro não encontrado na biblioteca.")


while True:

    if dias_v1 == False:
        dias_p_devolver1 -= 1
    if dias_v2 == False:
        dias_p_devolver2 -= 1
    if dias_v3 == False:
        dias_p_devolver3 -= 1
    if dias_v4 == False:
        dias_p_devolver4 -= 1
    if dias_v5 == False:
        dias_p_devolver5 -= 1

    print(f"""Olá! Bem-vindo(a) ao sistema de biblioteca.
    1. Adicionar Novo Livro
    2. Alugar Livro
    3. Consultar Prateleiras
    4. Devolver Livro
    5. Realocar Livro
    6. Remover Livro da Biblioteca
    7. Sair do sistema""")

    opcao = input("Digite um número correspondente à opção desejada para prosseguir: ")
    print("")

    if opcao == "1":
        titulo = input("Digite o título do livro: ").strip().capitalize()
        prateleira = input("Em qual prateleira você deseja adicionar? (1 a 5): ")
        mensagem = adicionar_livro(titulo, prateleira)
        print(mensagem)

    elif opcao == "2":
        print(consulta())
        alugar = input("Qual livro você deseja alugar? ").strip().capitalize()
        locador = input("Qual o nome do locador? ").strip().capitalize()
        dias = int(input("Por quantos dias você deseja alugar? "))
        print(aluga_livro(alugar, locador, dias))

    elif opcao == "3":
        print(consulta())

    elif opcao == "4":
        devolver = input("Qual livro você deseja devolver? ").strip().capitalize()
        devolver_livro(devolver)

    elif opcao == "5":
        renovar = realocar_livro()
        if renovar is not None:
            print(renovar)

    elif opcao == "6":
        remover = remover_livro()
        if remover is not None:
            print(remover)

    elif opcao == "7":
        print("Encerrando o sistema...")
        print("")
        break

    else:
        print("Opção inválida. Digite uma opção disponível.")