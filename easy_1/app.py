#!/usr/bin/env python3

cipher = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

cipher_int = [ord(i) - ord('A') for i in cipher]
key_int = [ord(i) - ord('A') for i in key]

print('picoCTF{' + ''.join(chr((cipher_int[i] - key_int[i]) %
                               26 + ord('A')) for i in range(11)) + '}')
