# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 00:15:13 2021

@author: YOULA Mohamed
"""

from sympy.logic.boolalg import to_cnf
from sympy.abc import a, b, c,d, e, f, g, h, i, j, k, l, m, o, p, q, r, s, t, u, v, w, x, y, z   

# ~r | (p & q)
# (~a | b) & (~b | c) & (~c | ~ a) & (a | ~d | f)
def result_1(r1):
    sc=''
    for J in range(len(list(r1))):    
        if r1[J] not in [' ','|','-','(',')']:
           if  r1[J-1] !='-':                    ## Atention
               sc=sc+' '+r1[J]
           else:
               sc=sc+' '+'-'+r1[J]
    print(sc+' 0')
    
def result_2(r1,p1): 
    result_1(r1)
    while '&' in p1:
         [r1,p1]= p1.split(" & ", 1)
         result_1(r1)
    result_1(p1)

####################
def nb_closes(kk):  
    counter = 1
    for letter in kk:
        if letter == "&":
            counter = counter + 1
    return counter    
##################
def Close_bin(r1):  
    counter = 0
    for letter in r1:
        if letter == "|":
            counter = counter + 1
    return counter 

def liste_closes(r1,p1):
    L=[]
    L.append(r1)
    while '&' in p1:
         [r1,p1]= p1.split(" & ", 1)
         L.append(r1)
    L.append(p1)
    return L     

def nb_closes_bin(liste):
    cl=0
    for elemt in liste:
        if Close_bin(elemt)==1:
           cl=cl+1
    return [cl,cl/len(liste)]  
###############################                   
def Close_Horn(r1):
    F=0
    ens=[' ','|','-','(',')']
    for J in range(len(list(r1))):       
        if r1[J] not in ens and r1[J-1]!='-' :
           F=F+1 
    return F

def nb_closes_Horn(liste):
    cl=0
    for elemt in liste:
        if Close_Horn(elemt) <=1 :
           cl=cl+1
    return [cl,cl/len(liste)]  
###############################
def Close_reverse_Horn(r1):
    F=0
    ens=[' ','|','-','(',')']
    for J in range(len(list(r1))):       
        if r1[J] not in ens and r1[J-1]=='-' :
           F=F+1 
    return F

def nb_Close_reverse_Horn(liste):
    cl=0
    for elemt in liste:
        if Close_reverse_Horn(elemt) <=1 :
           cl=cl+1
    return [cl,cl/len(liste)]           
            



def aff(E):
    T=to_cnf(E)
    kk='{}'.format((T))
    nb_clos=nb_closes(kk)
    C=[]
    for K in kk: 
        if K not in [' ','|','~','&','(',')']:
           C.append(K)
    C=sorted(list(set(C)))
    nb_var=len(C)
    kk=kk.replace('~','-')
    for I in range(len(C)):
        kk=kk.replace(C[I],str(C.index(C[I])+1))
    [r1, p1] = kk.split(" & ", 1)
    liste=liste_closes(r1,p1)
    
    print('----------------------------------------------------------------------------------')
    print(" c Nom de l'instance: formule")
    print(' p cnf'+' '+str(nb_var)+' '+str(nb_clos))
    print(result_2(r1,p1))
    print('----------------------------------------------------------------------------------')
    print('| Forme  CNF de la formule                              | '+str(T) )
    print('----------------------------------------------------------------------------------')
    print('| le nombre de variables                                | '+str(nb_var) ) 
    print('----------------------------------------------------------------------------------')
    print('| le nombre de closes                                   | '+str(nb_clos) )
    print('----------------------------------------------------------------------------------')
    print('| le nombre et la proportion de closes binaires         | '+str(nb_closes_bin(liste)))
    print('----------------------------------------------------------------------------------')
    print('| le nombre et la proportion de closes Horn             | '+str(nb_closes_Horn(liste)))
    print('----------------------------------------------------------------------------------')
    print('| le nombre et la proportion de closes reverse horn     | '+str(nb_Close_reverse_Horn(liste)))
    print('----------------------------------------------------------------------------------')

    
def main():
    """Le programme principal."""
     
    saisie1 = input('Saisissez votre formule: \n')
    s1= str(saisie1) 
    aff(s1)
    
if __name__ == "__main__":
    main()


    
