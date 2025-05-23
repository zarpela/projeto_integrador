from sympy import Matrix
import base64

K = Matrix([[3, 2], [1, 5]]) #codificadora
K_inv = Matrix([[217, 118], [59, 79]]) #inversa
mod = 256 #modulo


def str2ASCIItable(msg: str): #converter string em numero
    result = [ord(c) for c in msg] #para cada c em mensagem transforma c em ascii
    if len(result) % 2 != 0:
        result.append(ord(' '))  # Se o tamanho for ímpar, adiciona espaço (padding)
    return result

def ASCIItable2str(asciiINPUT: list): # inversa da de cima
    texto = [chr(c) for c in asciiINPUT] # Converte valores ASCII de volta para caracteres
    result = ""
    for i in texto:
        if i == " ":  # Remove os espaços de padding
            continue
        result += i
    return result

def encrypt(asciiINPUT: list):
    
    length = len(asciiINPUT)
    # Embaralha: primeiros os pares, depois os ímpares
    alternada = []
    for i in range(0, length, 2):  # pares
        alternada.append(asciiINPUT[i])
    for i in range(1, length, 2):  # ímpares
        alternada.append(asciiINPUT[i])

    # Reorganiza os valores
    half = length // 2 #divisao sem resto
    firstHalf = alternada[:half] # fatiamento
    secondHalf = alternada[half:]

    # Divide a Lista em duas metades
    A = Matrix((firstHalf, secondHalf))    # Cria uma matriz 2xN com as duas metades
    B = (K * A) % mod                      # Multiplica pela matriz codificadora e aplica módulo 256

    #Converte a matriz B (criptografada) de volta para uma lista linear de números.
    ascii_encrypted = []
    rows, cols = B.shape
    for col in range(cols):
        for row in range(rows):
            ascii_encrypted.append(int(B[row, col]))
 
    # Agora converte para bytes e depois para base64
    encrypted_bytes = bytes(ascii_encrypted)
    #print(ascii_encrypted) # printa os números encriptados pela matriz antes de passar por base 64
    encrypted_b64 = base64.b64encode(encrypted_bytes).decode('ascii')
    return encrypted_b64

def decrypt(b64_input: str):
    # Recebe a string criptografada em base64.
    encrypted_text = base64.b64decode(b64_input)  # Decodifica de base64 para bytes
    length = len(encrypted_text)  # Tamanho do texto criptografado
    asciiINPUT = list(encrypted_text)  # Transforma os bytes em lista de inteiros

    # Divide os valores em duas metades para reconstruir a matriz original embaralhada.
    firstHalf = []
    secondHalf = []
    for i in range(0, length, 2):
        firstHalf.append(asciiINPUT[i])
    for i in range(1, length, 2):
        secondHalf.append(asciiINPUT[i])
    
    B = Matrix((firstHalf, secondHalf))  # Cria matriz 2xN com os dados embaralhados
    A = (K_inv * B) % mod  # Multiplica pela inversa da matriz codificadora

    # Transforma novamente em ASCII
    ascii_list = []
    rows, cols = A.shape
    for col in range(cols):
        for row in range(rows):
            ascii_list.append(int(A[row, col]))

    # Converte SCII em texto
    texto = ASCIItable2str(ascii_list)
    return texto



if __name__ == "__main__":
    # Teste
    msg = input("mensagem: ")
    tabled = str2ASCIItable(msg)
    enc = encrypt(tabled)
    dec = decrypt(enc)

    print("Mensagem original:", msg)
    print("Criptografado:", enc)
    print("Descriptografado:", dec)   
    print((K*K_inv)%256) # outputa [[1, 0], [0, 1]] ( (K VEZES K^-1) em modulo 256 )
