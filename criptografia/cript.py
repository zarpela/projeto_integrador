from sympy import Matrix
import base64

K = Matrix([[3, 2], [1, 5]]) #codificadora
K_inv = Matrix([[217, 118], [59, 79]]) #inversa
mod = 256 #modulo

#print((K*K_inv)%256)

def str2ASCIItable(msg: str): #converter string em numero
    result = [ord(c) for c in msg] #para cada c em mensagem transforma c em ascii
    if len(result) % 2 != 0:
        result.append(ord(' '))  # padding
    return result

def ASCIItable2str(asciiINPUT: list): # inversa da de cima
    texto = [chr(c) for c in asciiINPUT]
    result = ""
    for i in texto:
        if i == " ":
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

    half = length // 2 #divisao sem resto
    firstHalf = alternada[:half] # fatiamento
    secondHalf = alternada[half:]

    A = Matrix((firstHalf, secondHalf))
    B = (K * A) % mod

    ascii_encrypted = []
    rows, cols = B.shape
    for col in range(cols):
        for row in range(rows):
            ascii_encrypted.append(int(B[row, col]))
 
    # Agora converte para bytes e depois para base64
    encrypted_bytes = bytes(ascii_encrypted)
    encrypted_b64 = base64.b64encode(encrypted_bytes).decode('ascii')
    return encrypted_b64

def decrypt(b64_input: str):
    encrypted_text = base64.b64decode(b64_input)
    asciiINPUT = list(encrypted_text)
    length = len(asciiINPUT)

    firstHalf = []
    secondHalf = []
    for i in range(0, length, 2):
        firstHalf.append(asciiINPUT[i])
    for i in range(1, length, 2):
        secondHalf.append(asciiINPUT[i])

    B = Matrix((firstHalf, secondHalf))
    A = (K_inv * B) % mod

    ascii_list = []
    rows, cols = A.shape
    for col in range(cols):
        for row in range(rows):
            ascii_list.append(int(A[row, col]))
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

