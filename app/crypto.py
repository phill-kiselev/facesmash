from Crypto.Cipher import XOR
import base64
import basehash

base62 = basehash.base62(8)

def encrypt(key, plaintext):
    #last_el = int(plaintext[plaintext.rfind('_')+1:])
    #encoded_last = base62.encode(last_el)
    #plaintext = plaintext[:plaintext.rfind('_')
    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(key, ciphertext):
  cipher = XOR.new(key)
  return cipher.decrypt(base64.b64decode(ciphertext)).decode('utf-8')
