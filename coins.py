# name of student: Timo de Gruiter
# number of student: 99067227
# purpose of program: school project  
# function of program: Calculating coins
# structure of program: Python

toPay = int(float(input('Amount to pay: '))* 100) # Hoeveel je moet betalen
paid = int(float(input('Paid amount: ')) * 100) # Hoeveel je hebt betaald
change = paid - toPay # berekend wat je terugkrijgt
overview = 'You got : '
if change > 0: # als het geld wat je terugkrijgt groter is dan 0
  coinValue = 50 # geeft een waarde van een munt
  
  while change > 0 and coinValue > 0: #Als beide meer zijn dan 0
    nrCoins = change // coinValue # de berekening

    if nrCoins > 0: #Als het meer is dan nul 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #print de tekst voor de munten
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #print de coins die je terug kunt krijgen
      change -= nrCoinsReturned * coinValue #de berekning hoeveel je kunt terugkrijgen 
      overview = str(overview) + str(nrCoins) + ' coin(s) of ' + str(coinValue) + ' cents. '

# comment on code below: Dit zijn alle munten die je mogelijk kunt terugkrijgen.
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #als change meer is dan 0
  print('Change not returned: ', str(change) + ' cents')
  
else:
  print(overview)
  print('done')