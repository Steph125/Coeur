from pyfirmata import Arduino, util
import time
def param():
 board = Arduino('COM7')
 test = True
 i=0
 led = []
 for m in range (2, 12):
   led.append(board.get_pin('d:' +str(m)+ ':o'))
 choix_affichage = 0
 choix = 0
 for n in range(2, 12):
   choix_affichage = int(input('Choix numero : '))
   print('Vous avez choisi l affichage :', choix_affichage)
   if choix_affichage == 1:
     while True:
       for i in range(2,12):
         led[i].write(1)
         time.sleep(0.5)
         led[i].write(0)
         time.sleep(0.5)
         i+2
   if choix_affichage == 2:
     while True:
       for i in range(2,12):
         led[i].write(1)
         time.sleep(0.5)
         led[i].write(0)
         time.sleep(0.5)
         i+3
   if choix_affichage == 3:
     while True:
       for i in range(2,12):
         led[i].write(1)
         time.sleep(0.5)
         led[i].write(0)
         time.sleep(0.5)
         i+4
   if choix_affichage == 4:
     while True:
       choix = int(input('Entrer le chiffre de la LED souhaitee'))
       print('Vous avez choisi la LED : ', choix)
       if choix > 10 or choix < 1:
         print('Error')
         print('S il vous plait bien vouloir choisir une LED comprise entre 1 et 10')
       else:
         while True:
           led[choix].write(1)
           time.sleep(1)
           led[choix].write(0)
           time.sleep(1)
   if choix_affichage == 5:
     while True:
       for i in range(2,12):
         led[i].write(1)
         time.sleep(0.03)
         led[i+1].write(0)
         time.sleep(0.5)
         led[i].write(0)
         time.sleep(0.5)
         led[i+1].write(1)
         time.sleep(0.5)
         i+1
   if choix_affichage == 6:
     while True:
       for i in range(2,12):
         led[i].write(1)
         time.sleep(0.5)
         i+1
       for i in range(2,12):
         led[i].write(0)
         time.sleep(0.5)
         i+1
   board.exit()
