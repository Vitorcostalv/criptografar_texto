def criptografar_texto(texto):
    return [ord(char) for char in texto]

def main():
    texto_usuario = input("Digite um texto para criptografar: ")
    criptografado = criptografar_texto(texto_usuario)
    print("\nTexto original:", texto_usuario)
    print("Texto criptografado (valores numéricos):", criptografado)

if __name__ == "__main__":
    main()
