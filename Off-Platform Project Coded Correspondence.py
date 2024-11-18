#1 Caesar Cipher
import string

complete_message = """Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. 

For example, if I chose an offset of 3 and a message of "hello", I would encode my message by shifting each letter 3 places to the left with respect to the alphabet. So "h" becomes "e", "e" becomes "b", "l" becomes "i", and "o" becomes "l". Then I have my encoded message, "ebiil"! Now I can send you my message and the offset and you can decode it by shifting each letter 3 places to the right. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer encoded message that you have to decode yourself!
    
    xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
    
This message has an offset of 10. Can you decode it?"""

decode_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

abc = string.ascii_lowercase #lista del abecedario

#Decodifcación Caesar by Mapache
def caesar_decode(message, offset):
  position = 0;
  decoded = [];

  for letter in message: #loop en el mensaje
    after = ""; #variable para permitir NO repetir agregar NO letras
    for count in abc: #loop en el abecedario
      if count == letter and letter.isalpha(): #encontrar posición de letra en alfabeto AND poner solo letras en el mensaje decodificado
        position = abc.find(letter)
        if (position + offset) >= len(abc):
          decoded.append(abc[position + offset - len(abc)])
        else: decoded.append(abc[position + offset])
      elif not letter.isalpha() and not after == letter: #incluir NO letras
        decoded.append(letter)
        after = letter

  return decoded

message1_decode = "".join(caesar_decode(decode_message,10))
print(message1_decode) #hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!

#2
#Codifcación Caesar by Mapache
def caesar_encode(message, offset):
  position = 0;
  encoded = [];

  for letter in message: #loop en el mensaje
    after = ""; #variable para permitir NO repetir agregar NO letras
    for count in abc: #loop en el abecedario
      if count == letter and letter.isalpha(): #encontrar posición de letra en alfabeto AND poner solo letras en el mensaje decodificado
        position = abc.find(letter)
        encoded.append(abc[position - offset])
      elif not letter.isalpha() and not after == letter: #incluir NO letras
        encoded.append(letter)
        after = letter

  return encoded

print("".join(caesar_encode("Hola Vishal, logre construir mi propio decodificador Caesar jejeje",10)))

#3
first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
        
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print("".join(caesar_decode(first_message,10))) #the offset for the second message is fourteen.
print("".join(caesar_decode(second_message,14))) #performing multiple caesar ciphers to code your messages is even more secure!

#4
complete_message = """Hello again friend! I knew you would love the Caesar Cipher, it's a cool, simple way to encrypt messages. Did you know that back in Caesar's time, it was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift? That's all changed with computers! Now we can brute force these kinds of ciphers very quickly, as I'm sure you can imagine.
            
To test your cryptography skills, this next coded message is going to be harder than the last couple to crack. It's still going to be coded with a Caesar Cipher but this time I'm not going to tell you the value of the shift. You'll have to brute force it yourself.
            
Here's the coded message:
            
    vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
            
Good luck!"""

decode_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

message2_decode = "".join(caesar_decode(decode_message,7)) #descubierto al azar: 7 es el ofset del mensaje
print(message2_decode)