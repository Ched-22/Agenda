def adicionar_contato(contatos, nome_contato, telefone, email):
    contato = {"nome_contato": nome_contato,
               "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print("O contato {} foi adicionado com sucesso!".format(nome_contato))
    return


"""def adicionar_contato(contatos, nome_contato):
    contato = {"contato": nome_contato, "favorito": False}
    contatos.append(contato)
    print("O contato {} foi adicionado com sucesso!".format(nome_contato))
    return"""


def ver_contatos(contatos):
    print("Ver lista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["favorito"] else " "
        nome_contato = contato["nome_contato"]
        telefone = contato["telefone"]
        email = contato["email"]
        print("{} [{}] {}".format(indice, status,
              nome_contato, telefone, email))
    return


def editar_contato(contatos, indice_contato, novo_nome_contato):
    indice_contato_editato = int(indice_contato) - 1
    if indice_contato_editato >= 0 and indice_contato_editato < len(contatos):
        contatos[indice_contato_editato]["nome_contato"] = novo_nome_contato
        print("O contato {} foi atualizado para {}".format(
            indice_contato, novo_nome_contato))
    else:
        print("Indice do contato inválido")
    return


def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = True
    print("O contato {} foi marcado como favorito".format(indice_contato))
    return


def desfavoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = False
    print("O contato {} foi desmarcado como favorito".format(indice_contato))
    return


def ver_contatos_favoritos(contatos):
    print("Lista de contatos favoritos")
    favoritos = []
    for contato in contatos:
        if contato["favorito"]:
            favoritos.append(contato)

    if favoritos:
        for indice, contato in enumerate(favoritos, start=1):
            print("{} [{}] ".format(indice, contato["nome_contato"]))
    else:
        print("não há contatos favoritos")
    return


def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato_removido = contatos.pop(indice_contato_ajustado)
        print("O contato {} foi removido com sucesso!".format(
            contato_removido["nome_contato"]))
    else:
        print("Índice de contato inválido!")
    return


contatos = []

while True:
    print("\nAgenda de Contatos")
    print("1. Adicionar Contato\n2. Ver Contatos Cadastrados\n3. Editar contato\n4. Marcar/desmarcar contato como Favorito\n5. Ver contatos Favoritos\n6. Deletar Contato\n7. Sair")

    escolha = int(input("Digite a sua escolha: "))
    if escolha < 1 or escolha > 7:
        print("Opção inválida, tente novamente!")
        continue

    if escolha == 1:
        nome_contato = input("Digite o nome do novo contato: ")
        telefone = input("Digite o telefone do novo contato: ")
        email = input("Digite o email do novo contato: ")
        adicionar_contato(contatos, nome_contato, telefone, email)

    elif escolha == 2:
        ver_contatos(contatos)

    elif escolha == 3:
        ver_contatos(contatos)
        indice_contato = input(
            "Digite o indice do contato que deseja atualizar: ")
        novo_contato = input("Digite o novo nome do contato: ")
        editar_contato(contatos, indice_contato, novo_contato)

    elif escolha == 4:
        ver_contatos(contatos)
        indice_contato = input(
            "Digite o indice do contato que deseja favoritar/desfavoritar: ")
        print("1. Favoritar Contato\n2. Desfavoritar Contato")
        favoritar_desfavoritar = input(
            "Digite a opção para favoritar ou desfavoritar o contato: ")
        if favoritar_desfavoritar == "1":
            favoritar_contato(contatos, indice_contato)
        elif favoritar_desfavoritar == "2":
            desfavoritar_contato(contatos, indice_contato)

    elif escolha == 5:
        ver_contatos_favoritos(contatos)

    elif escolha == 6:
        ver_contatos(contatos)
        indice_contato = input(
            "Digite o indice do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)

    elif escolha == 7:
        break
print("Programa finalizado")
