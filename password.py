def password_validator(password):
  return password == "zaza"

password = input("saisir mot de passe: ")

if password_validator(password):
  print("c'est ok!")
else:
  print("ah gars...")