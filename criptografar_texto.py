def criptografar_texto(texto):
    return [ord(char) for char in texto]

def descriptografar_texto(valores):
    return ''.join(chr(num) for num in valores)

def main():
    print("Escolha uma opção:")
    print("1. Criptografar um texto")
    print("2. Descriptografar um texto")
    
    escolha = input("Digite 1 ou 2: ")
    
    if escolha == '1':
        texto_usuario = input("\nDigite um texto para criptografar: ")
        criptografado = criptografar_texto(texto_usuario)
        print("\nTexto original:", texto_usuario)
        print("Texto criptografado (valores numéricos):", criptografado)
    elif escolha == '2':
        valores_usuario = input("\nDigite os valores numéricos separados por espaço: ")
        valores = list(map(int, valores_usuario.split()))
        descriptografado = descriptografar_texto(valores)
        print("\nValores numéricos:", valores)
        print("Texto descriptografado:", descriptografado)
    else:
        print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
