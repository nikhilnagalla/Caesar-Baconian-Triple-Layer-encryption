baconian_dict = {
  'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
  'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
  'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
  'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
  'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
  'Z': 'BBAAB',
    }

def reverse_string(text):
  return text[::-1]
def baconian_encrypt(text):
    result = ''
    for character in text:
        if character.upper() in baconian_dict:
            result += baconian_dict[character.upper()] 
        elif character == ' ':
            result += ' '

    return result.strip()

def baconian_decrypt(ciphertext):
  baconian_dict = {
      'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
      'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'J',
      'ABABA': 'K', 'ABABB': 'L', 'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O',
      'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
      'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X', 'BBAAA': 'Y',
      'BBAAB': 'Z',
  }

  result = ''
  current_code = ''
  for char in ciphertext:
      if char == ' ':
          result += ' '
      else:
          current_code += char
          if len(current_code) == 5:
              result += baconian_dict.get(current_code, current_code)
              current_code = ''

  return result

def tri_layer_encrypt(text):
  reverse=reverse_string(text)
  caesar_reverse=caesar_cipher(reverse,2)
  baconian_caesar_reverse=baconian_encrypt(caesar_reverse)
  return baconian_caesar_reverse 


  
def tri_layer_decrypt(text):
  re=baconian_decrypt(text)
  resu=caesar_cipher(re,-2)
  result=reverse_string(resu)
  return result




  
  


 
# printing result 





#Our main function which does the shifting
def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Shift the character by the specified amount
            shifted = ord(char) + shift - ord('a')
            shifted = shifted % 26 + ord('a')
            
            # Convert back to uppercase if the original character was uppercase
            if is_upper:
                shifted = chr(shifted).upper()
            else:
                shifted = chr(shifted)
            
            result += shifted
        else:
            # If the character is not a letter, keep it unchanged
            result += char

    return result




def setup():
  message=input("Enter what you want to be decoded or encoded:")
  clost=["Caesar Cipher Encrypt CCE,","Caesar Cipher Decrypt CCD","Baconian Cipher Encrypt BCE","Baconian Cipher Decrypt BCD","Triple Layer Encryptio TLE","Triple Layer Decryption TLD","Exit"]
  print("Do you want to use:")
  for i in clost:
    print(i)
  choice_1=input("")
  choice_1=choice_1.lower()
  
  if choice_1=="cce" or choice_1=="caesar cipher encrypt":
    shift=int(input("Enter your shift value"))
    print(caesar_cipher(message, shift))
    setup()
  elif choice_1=="ccd" or choice_1=="caesar cipher decrypt":
    shift=int(input("Enter your shift value"))
    print(caesar_cipher(message,-shift))
    setup()
  elif choice_1=="bce" or choice_1=="baconian cipher encrypt":
    print(baconian_encrypt(message))
    setup()
  elif choice_1=="bcd" or choice_1=="baconian cipher decrypt":
    print(baconian_decrypt(message))
    setup()
  elif choice_1=="triple layer encryption" or choice_1=="tle":
    print(tri_layer_encrypt(message))
    setup()
  elif choice_1=="triple layer decryption" or choice_1=="tld":
    print(tri_layer_decrypt(message))
    setup()
  elif choice_1=="e" or choice_1=="exit":
    print("Ok Bye")
  else:
    print("Error pls Try again")
    setup()
    
      

setup()

