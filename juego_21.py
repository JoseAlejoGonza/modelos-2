import random
import math
          
def juego(baraja,mazoA,rnd,x):
    if(len(baraja)<=52):
        if(len(mazoA)>=1 and x>1):
            baraja.append(mazoA[rnd])
            mazoA.pop(rnd)
            baraja(baraja,mazoA,math.floor(random.randrange(0,x-1)),x-1)
    return baraja
 
def jugador(juego, mJugador,mBanca):
    print("Mano Jugador: ", mJugador)    
    if(len(mJugador)<2 and len(mBanca)<2):
        jugador(juego[2:],mJugador+[juego[0]]+[juego[1]],mBanca+[juego[0]]+[juego[1]])
    else:
        if(comprobar_mano(mJugador)<=21):            
            if(comprobar_mano(mJugador)==21):
                print("Ganó")
            elif(input("desea una carta?  ")==('s' or 'S')):
                print(len(mJugador))
                jugador(juego[1:],mJugador+[juego[0]],mBanca+[juego[math.floor(random.randrange(0,52))]])                
            else:
                print("Mano Jugador: ", mJugador)
                print(comprobar_mano(mJugador))
                print("Mano Banca : ", mBanca)
                print(comprobar_mano_AI(mBanca))
                if(comprobar_mano_AI(mBanca)> comprobar_mano(mJugador) and comprobar_mano_AI(mBanca)<=21):
                     print("perdió")
                elif(comprobar_mano(mJugador)>comprobar_mano_AI(mBanca) and comprobar_mano(mJugador)<=21) or comprobar_mano_AI(mBanca)>21:     
                     print("Ganó")
        else:
            print(comprobar_mano(mJugador))
            print("perdó")

def comprobar_mano(baraja):    
    if(baraja==[]):
        return 0
    else:
        return baraja[0] + comprobar_mano(baraja[1:])
    
def comprobar_mano_AI(baraja):    
    if(baraja==[]):
        return 0
    else:
        return baraja[0] + comprobar_mano_AI(baraja[1:])
        
jugador(juego([],[1,1,1,1,2,2,2,2,
                   3,3,3,3,4,4,4,4,
                   5,5,5,5,6,6,6,6,
                   7,7,7,7,8,8,8,8,
                   9,9,9,9,10,10,10,10
                   10,10,10,10,
                   10,10,10,10,
                   10,10,10,10

                   ],
        math.floor(random.randrange(0,52)),52),[math.floor(random.randrange(1,10)),math.floor(random.randrange(1,10))],[math.floor(random.randrange(1,10)),math.floor(random.randrange(1,10))])

