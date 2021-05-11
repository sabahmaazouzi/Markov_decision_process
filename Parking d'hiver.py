import numpy as np
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Initialisation
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
gamma = 0.9
green = (0,3)
red = (1,3)
S = { (i, j) for j in range(4) for i in range(3) }
rewarads = { s:0 for s in S }
rewarads[green] = 1 # case verte
rewarads[red] = -100 # case rouge
actions = { s:('U', 'D', 'L', 'R') for s in S}
##actions[ (0,0) ] = ('D', 'R')
##actions[ (2,3) ] = ('U', 'L')
politique = { s: np.random.choice( actions[s] ) for s in S}
V = { s:0 for s in S}
print(actions)
V[green] = 1
V[red] = -100


actions[(1,0)] = ('U', 'D')
actions[(1,1)] = ()
actions[(1,2)] = ('U', 'D','R')
actions[(1,3)] = ('U', 'D','L')



actions[ (0,0) ] = ('D', 'R')
actions[ (0,1) ] = ('L', 'R')
actions[ (0,2) ] = ('D', 'L', 'R')
actions[ (0,3) ] = ('L', 'D')



actions[(2,0)] = ('U', 'L')
actions[(2,1)] = ('U', 'L', 'R')
actions[(2,2)] = ('U', 'L', 'R')
actions[(2,3)] = ('U', 'R')


actions[(2,0)] = ('U', 'R')
actions[(2,1)] = ('L', 'R')
actions[(2,2)] = ('U', 'L', 'R')
actions[(2,3)] = ('U', 'L')


dirc = ('U', 'D', 'L', 'R')

direction ={i:('U', 'R') for i in dirc }
direction['U']=direction['D']=('L', 'R')
direction['R']=direction['L']= ('U', 'D')

def indice(d):
    if d == 'R':
        return (0,1)
    else:
        if d == 'L':
            return (0,-1)
        else:
            if d == 'U':
                return (-1,0)
    return (1,0)
            
#la fonction valeur_case retourne l'indice approrie dans v

def valeur_case(case,d):
    a = actions[case]
    b = indice(d) 
    s= (case[0]+b[0] ,case[1]+b[1] )
    if d in a :
        return s 
       
   
    return case 
            

# CALCUL AVEC LE NOMBRE DES ITÉRATIONS 
def calcul_valeur(n_iteration):
    
    dict_valeur = V.copy()
    V_=V.copy()
    for i in range(n_iteration):
        for case in V :
            max_ = [ ]
            #a = actions[case]
            for t in range(4) :
                b= direction[dirc[t]]
                max_.append(0.8*dict_valeur[valeur_case(case,dirc[t])]+0.1*(dict_valeur[valeur_case(case,b[0])]+dict_valeur[valeur_case(case,b[1])]))
            if i == n_iteration -1 :
                maxim_ =   max_.index(max(max_))
                politique[case]=dirc[maxim_]
            
            
            V_[case]=rewarads[case]+0.9*max(max_)
            #print(case, max_)
        dict_valeur = V_.copy()
    print(V_)
    print(politique)



calcul_valeur(5)

# CALCUL en choisissant une  marge entre la max de la matrice V entre deux itérations succesive 
def calcul_valeur2(eps):
    dict_valeur = V.copy()
    V_=V.copy()
    bol  = True 
    nom=0
    max_ = [ ]
    while  bol > eps  :
        v1=max([V_[e] for e in V_ ])
        for case in V :
            max_ = [ ]
            a = actions[case]
            for t in range(4) :
                b= direction[dirc[t]]
                max_.append(0.8*dict_valeur[valeur_case(case,dirc[t])]+0.1*(dict_valeur[valeur_case(case,b[0])]+dict_valeur[valeur_case(case,b[1])]))
           
            
            V_[case]=rewarads[case]+0.9*max(max_)
        v0=max([V_[e] for e in V_ ])
            #print(case, max_)
        dict_valeur = V_.copy()
        bol  = v0-v1 
       
    maxpo_=0    
    for case in V :
       
        maxpo =   max_.index(max(max_))
        politique[case]=dirc[maxpo]
            
    print(V_)
    print(politique)



calcul_valeur2(0.00000001)
