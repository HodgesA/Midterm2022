def main():
  user = {}
  choice = 0
  for i in range(100):
    choice = getChoice
    if  choice == 9:
      Everyone(user)
    if choice ==13:
      Eplus(user)
    if choice== 17:
      Teen(user)
    if choice == 21:
      Mature(user)
#Get choice from user
def getChoice():
  print('Enter Your Age')
  print('-------------------')
  print('9 and under - Everyone')
  print('10 - 13 = Eplus')
  print('14 - 17 = Teen')
  print('18plus = Mature')
  #try/except method for choices
  try:
    age = int(input('Enter Your Age: '))
    while age < 1 or age > 100:
      print('ERROR')
      age = int(input('Enter Your Age:'))
    return age

  except:
    print('Invalid input, ,must be under 100 years old')
#assign games to ratings
def Everyone(user):
  print ("These are the best games for you: Super Mario & Flight Simulator")
def Eplus(user):
  print ("These are the best games for you: Horizon: Forbidden & Far Cry Primal")
def Teen(user):
   print ("These are the best games for you: Final Fantasy & Uncharted")
def Mature(user):
   print ("These are the best games for you: Grand Theft Auto & Battlefield")
  #return main function
main()