from __init__ import gerar_senha_aleatoria, gerar_senha_frase, validar_complexidade_senha

if __name__ == '__main__':
    t = int(input("quantos caracteres na senha? "))
    ma = input("letras maíusculas (S/N)? ").upper()
    mi = input("letras minúsculas (S/N)? ").upper()
    di = input("digitos (S/N)? ").upper()
    si = input("Simbolos (S/N)? ").upper()
    rc = input("Remover simbolos que podem confundir (S/N)? ").upper()

    senha = gerar_senha_aleatoria(tamanho=t)
    rc = input("")
