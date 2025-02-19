from __init__ import gerar_senha_aleatoria, gerar_senha_frase, validar_complexidade_senha

from werkzeug.security import generate_password_hash, check_password_hash

if __name__ == '__main__':

    print("digite:")
    print("1 para gerar uma senha aleatória")
    print("2 para gerar uma senha de frase")
    print("3 para validar a complexidade de uma senha")

    opcao = int(input("digite uma opção:"))

    if opcao == 1:

        print("gerando uma senha aleatória:")

        t = int(input("quantos caracteres na senha? "))
        ma = input("letras maiúsculas (S/N)? ").upper()
        mi = input("letras minúsculas (S/N)? ").upper()
        di = input("dígitos (S/N)? ").upper()
        si = input("Símbolos (S/N)? ").upper()
        rc = input("Remover símbolos que podem confundir (S/N)? ").upper()

        senha = gerar_senha_aleatoria(tamanho=t,
                                      maiusculas=True if ma == "S" else False,
                                      minusculas=True if mi == "S" else False,
                                      digitos=True if di == "S" else False,
                                      simbolos=True if si == "S" else False,
                                      remove_confusos=True if rc == "S" else False)
        if senha is None:
            print("impossível criar senha")
        else:
            print(f"senha criada com sucesso: {senha}")

    elif opcao == 2:

        print("gerando uma senha de frase:")

        t = int(input("quantos palavras na senha? "))
        co = input("palavras completas (S/N)? ").upper()
        ma = input("letras maiúsculas (S/N)? ").upper()
        se = input("qual separador usar? ")[:1]

        senha = gerar_senha_frase(num_palavras=t,
                                  palavras_completas=True if co == "S" else False,
                                  separador=se,
                                  maiusculas=True if ma == 'S' else False)

        if senha is None:
            print("impossível criar senha")
        else:
            print(f"senha criada com sucesso: {senha}")

    else:
        print("testando a complexidade da senha:")

        senha = input("digite uma senha para testar: ")
        t = int(input("quantos caracteres na senha? "))
        ma = input("letras maiúsculas (S/N)? ").upper()
        mi = input("letras minusculas (S/N)? ").upper()
        di = input("dígitos (S/N)? ").upper()
        si = input("Símbolos (S/N)? ").upper()

        teste = validar_complexidade_senha(senha,
                                           tamanho=t,
                                           maiusculas=True if ma == "S" else False,
                                           minusculas=True if mi == "S" else False,
                                           digitos=True if di == "S" else False,
                                           simbolos=True if si == "S" else False)

        if teste:
            print("senha complexa e valida")
        else:
            print("sua senha é fraca")

        cifrada = generate_password_hash(senha)
        print(f"senha cifrada: {cifrada}")

        senha = input("digite uma senha para testar: ")

        igual = check_password_hash(cifrada, senha)

        if igual:
            print("senha correta")
        else:
            print("senha incorreta")
