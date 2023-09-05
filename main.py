"""A module full of functions for encoding and decoding messages from classical ciphers.
Ciphers found at en.wikipedia.org/wiki/Category:Classical_ciphers. https://inventwithpython.com/cracking/"""

#git enabled. press "git" in tools -Koko

#for offset cypher
ALPHA1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
AlPHA2 = ':;/|!@#$%^&*()_+-=}{][?><,."'
ALPHABET = ALPHA1 + AlPHA2
n = 0 # for offset cypher

  
def adfgvx():
  """The ADFGVX cipher. Informations at en.wikipedia.org/wiki/ADFGVX_cipher."""

#offset cypher

def offset_cipher():
  """an offset cypher I made -Koko"""
  cipher_text = input("enter top secret info: ")
  offset_number = int(input("select offset key (must be number): "))
  output = ""
  for x in cipher_text:
    n = 0
    while x != ALPHABET[n]:
      n += 1
    n = str(n + offset_number)
    output = output + n + "/"
    n = int(n)
  print(output)
offset_cipher()
