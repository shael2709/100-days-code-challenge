alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ""
message = input("please enter your message:")
for character in message:
 if character in alphabet:
  position = alphabet.find(character)
  newPosition = (position + key) % 26
  newCharacter = alphabet[newPosition]
  newMessage += newCharacter
 else:
      newMessage += character
print("The new message is:", newMessage)
