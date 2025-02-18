from __init__ import gerar_senha_aleatoria, gerar_senha_frase, validar_complexidade_senha

from werkzeug.security import generate_password_hash, check_password_hash

if __name__ == '__main__':
    t = int(input("quantos caracteres na senha? "))
    ma = input("letras maíusculas (S/N)? ").upper()
    mi = input("letras minúsculas (S/N)? ").upper()
    di = input("digitos (S/N)? ").upper()
    si = input("Simbolos (S/N)? ").upper()
    rc = input("Remover simbolos que podem confundir (S/N)? ").upper()

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

    t = int(input("quantos palavras na senha? "))
    co = input("palavras completas (S/N)? ").upper()
    ma = input("letras maíusculas (S/N)? ").upper()
    se = input("qual separador usar? ")[:1]

    senha = gerar_senha_frase(num_palavras=t,
                              palavras_completas=True if co == "S" else False,
                              separador=se,
                              maiusculas=True if ma == 'S' else False)

    if senha is None:
        print("impossível criar senha")
    else:
        print(f"senha criada com sucesso: {senha}")

    senha = input("digite uma senha para testas: ")
    t = int(input("quantos caracteres na senha? "))
    ma = input("letras maisculas (S/N)? ").upper()
    mi = input("letras minusculas (S/N)? ").upper()
    di = input("digitos (S/N)? ").upper()
    si = input("Simbolos (S/N)? ").upper()

    


