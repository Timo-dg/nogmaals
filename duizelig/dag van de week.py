print('ma', 'di', 'wo', 'do', 'vr', 'za', 'zo')
dag = input('Kies een dag: ').lower()

if dag == 'ma':
    dag = 1
if dag == 'di':
    dag = 2
if dag == 'wo':
    dag = 3
if dag == 'do':
    dag = 4
if dag == 'vr':
    dag = 5
if dag == 'za':
    dag = 6
if dag == 'zo':
    dag = 7
getal = 1
while getal <= dag:
    if getal == 1:
        naam = 'ma'
    if getal == 2:
        naam = 'di'
    if getal == 3:
        naam = 'wo'
    if getal == 4:
        naam = 'do'
    if getal == 5:
        naam = 'vr'
    if getal == 6:
        naam = 'za'
    if getal == 7:
        naam = 'zo'
    
    print(naam)
    getal = getal + 1



    

# dagen = ['ma', 'di', 'wo', 'do', 'vr', 'za', 'zo'] 
# input(dagen )
# while in dagen:
#     print(dagen)