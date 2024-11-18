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
    position = abc.find(letter) #encontrar posición de letra en alfabeto
    if letter.isalpha(): #poner solo letras en el mensaje decodificado        
      decoded.append(abc[position + offset - len(abc)])       
    elif not letter.isalpha() and not after == letter: #incluir NO letras
      decoded.append(letter)
      after = letter

  return "".join(decoded)

message1_decode = caesar_decode(decode_message,10)
print(message1_decode) #hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!

#2
#Codifcación Caesar by Mapache
def caesar_encode(message, offset):
  position = 0;
  encoded = [];

  for letter in message: #loop en el mensaje
    after = ""; #variable para permitir NO repetir agregar NO letras
    position = abc.find(letter) #encontrar posición de letra en alfabeto
    if letter.isalpha(): #encontrar posición de letra en alfabeto AND poner solo letras en el mensaje decodificado
      encoded.append(abc[position - offset])
    elif not letter.isalpha() and not after == letter: #incluir NO letras
      encoded.append(letter)
      after = letter

  return "".join(encoded)

print(caesar_encode("Hola Vishal, logre construir mi propio decodificador Caesar jejeje",10))

#3
first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
        
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print(caesar_decode(first_message,10)) #the offset for the second message is fourteen.
print(caesar_decode(second_message,14)) #performing multiple caesar ciphers to code your messages is even more secure!

#4
complete_message = """Hello again friend! I knew you would love the Caesar Cipher, it's a cool, simple way to encrypt messages. Did you know that back in Caesar's time, it was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift? That's all changed with computers! Now we can brute force these kinds of ciphers very quickly, as I'm sure you can imagine.
            
To test your cryptography skills, this next coded message is going to be harder than the last couple to crack. It's still going to be coded with a Caesar Cipher but this time I'm not going to tell you the value of the shift. You'll have to brute force it yourself.
            
Here's the coded message:
            
    vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
            
Good luck!"""

decode_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

message2_decode = caesar_decode(decode_message,7) #descubierto al azar: 7 es el ofset del mensaje
print(message2_decode)

#5 Vigenère Cipher
complete_message = """Salutations! As you can see, technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy, and us crypto-enthusiasts have had to get more creative and use more complicated ciphers. This next cipher I'm going to teach you is the Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso (cool name eh?) in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.
            
The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword.
           
Consider the message:
           
    barry is the spy

If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
           
    dog
               
Now we repeat the keyword over and over to generate a keyword phrase that is the same length as the message we want to code. So if we want to code the message "barry is the spy" our keyword phrase is "dogdo gd ogd ogd". Now we are ready to start coding our message. We shift each letter of our message by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth.

              message:    b  a  r  r  y    i  s    t  h  e    s  p  y
                
       keyword phrase:    d  o  g  d  o    g  d    o  g  d    o  g  d
                 
resulting place value:    24 12 11 14 10   2  15   5  1  1    4  9  21
      
So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us a place value of 24, which is "y". Remember to loop back around when we reach either end of the alphabet! Then continue the trend: we shift "a" by the place value of "o", 14, and get "m", we shift "r" by the place value of "g", 6, and get "l", shift the next "r" by 3 places and get "o", and so forth. Once we complete all the shifts we end up with our coded message:
            
    ymlok cp fbb ejv
                
As you can imagine, this is a lot harder to crack without knowing the keyword! So now comes the hard part. I'll give you a message and the keyword, and you'll see if you can figure out how to crack it! Ready? Okay here's my message:
            
    txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!
                
and the keyword to decode my message is 
            
    friends
                
Because that's what we are! Good luck friend!"""

decode_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
key_word = "friends"

def vigenere_decode(message,key):
  position1 = 0;
  position2 = 0;
  decoded = [];
  count = 0 #posición inicial de la clave
  
  for letter in message: #loop en el mensaje
    after = "" #variable para permitir NO repetir agregar NO letras
    position1 = abc.find(letter) #encontrar posición de letra en alfabeto
    position2 = abc.find(key[count]) #encontrar posición de letra de la keyword en alfabeto
    if letter.isalpha() and count < len(key)-1: #poner solo letras en el mensaje decodificado        
      decoded.append(abc[position1 + position2 - len(abc)])   
      count += 1   
    elif not letter.isalpha() and not after == letter and count < len(key): #incluir NO letras
      decoded.append(letter)
      after = letter
    else: 
      decoded.append(abc[position1 + position2 - len(abc)])
      count = 0

  return "".join(decoded)

message3_decode = vigenere_decode(decode_message,key_word)
print(message3_decode) 

#6
def vigenere_encode(message,key):
  position1 = 0;
  position2 = 0;
  encoded = [];
  count = 0 #posición inicial de la clave
  
  for letter in message: #loop en el mensaje
    after = "" #variable para permitir NO repetir agregar NO letras
    position1 = abc.find(letter) #encontrar posición de letra en alfabeto
    position2 = abc.find(key[count]) #encontrar posición de letra de la keyword en alfabeto
    if letter.isalpha() and count < len(key)-1: #poner solo letras en el mensaje decodificado        
      encoded.append(abc[position1 - position2])   
      count += 1   
    elif not letter.isalpha() and not after == letter and count < len(key): #incluir NO letras
      encoded.append(letter)
      after = letter
    else: 
      encoded.append(abc[position1 - position2])
      count = 0

  return "".join(encoded)

print(vigenere_encode(message3_decode,"elpepe")) #se codifica el mensaje con la palabra "elpepe"
