def cipher(plaintext, key): 
    result = "" 
    matrix = [["" for _ in range(len(plaintext))] for _ in range(key)] 
    increment = 1 
    row = 0 
    col = 0 
 
    for p in plaintext: 
        if row + increment < 0 or row + increment >= len(matrix): 
            increment = increment * -1 
            
 
        matrix[row][col] = p 
        row += increment 
        col += 1 
 
    print("Encryption Matrix:") 
    for row in matrix: 
        print(row) 
 
    for row in matrix: 
        result += "".join(row) 
    return result 
 
 
def decipher(ciphertext, key): 
    result = "" 
    matrix = [["" for _ in range(len(ciphertext))] for _ in range(key)] 
    idx = 0 
    increment = 1 
 
    for selectedRow in range(0, len(matrix)): 
        row = 0 
 
        for col in range(0, len(matrix[row])): 
            if row + increment < 0 or row + increment >= len(matrix): 
                increment = increment * -1 
 
            if row == selectedRow: 
                matrix[row][col] += ciphertext[idx] 
                idx += 1 
 
            row += increment 
 
    print("\nDecryption Matrix:") 
    for row in matrix: 
        print(row) 
 
    matrix = transpose(matrix) 
    for row in matrix: 
        result += "".join(row) 
    return result 
 
 
def transpose(m): 
    result = [["" for _ in range(len(m))] for _ in range(len(m[0]))] 
    for i in range(len(m)): 
        for j in range(len(m[0])): 
            result[j][i] = m[i][j] 
    return result 
 
 
def main(): 
    print("RailFence Cipher") 
    plaintext = input("Enter the Plaintext: ") 
    key = int(input("Enter the no. of rails: ")) 
    ciphertext = cipher(plaintext, key) 
    print("\nCiphered text: {0}".format(ciphertext)) 
    deciphertext = decipher(ciphertext, key) 
    print("\nDeciphered text: {0}".format(deciphertext)) 
    return

main()