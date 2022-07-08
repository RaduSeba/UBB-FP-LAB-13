n=int(input("Numarul de puncte din plan:"))



"""
Generez toate variantele posibile(combinari sau permjutari sau produs cartezian trebe sa imi dau seama),apoi fac ecuatia dreptei 
dintre 2 puncte si pentru restul punctelor verific daca sunt pe dreapta si afisez solutia
{U(Xk,Yk),k apartine I|I apartine P(n)}-spatiu de cautare
2^n-primele 3 combinari      posibilitati
candidatul este un punct din plan de coordonate x si y

"""
def panta(x1,x2,y1,y2):
    m = int((int(y2)-int(y1))/(int(x2)-int(x1)))
    return m


x=[]
y=[]
l=[]
def citire(n):
    for i in range(0,n):
        a=input("Abscisa numarului:")
        x.append(a)
        b=input("Ordonata numarului:")
        y.append(b)
        l1=[a,b]
        l.append(l1)  

citire(n)
def iterativ():
    for i in range(0,len(l)-2):
        for j in range(i+1,len(l)-1):
            m=panta(x[i],x[j],y[i],y[j])
            lista=[l[i],l[j]]
            listafinala=[]
            k=j+1
            while k<len(l):
                n=panta(x[k],x[j],y[k],y[j])
                if m==n:
                    lista.append(l[k])
                    listafinala.append(lista) 
                if len(lista)>2:    
                    print(lista)
                else :
                    print("Nu exista puncte")            
                k=k+1    



def panta2(x, y):
    """
    Functia pentru determinarea pantei dintre 2 puncte
    """
    if int(y[0])-int(x[0]) == 0:
        return -1

    d = (int(y[1])-int(x[1]))/(int(y[0])-int(x[0]))
    return d

def recursiv():

    main_list = l
    print_list = [l[0], l[1]]
    rec(0, 1, 2, main_list, print_list)


def rec(i, j, k, lista, print_list):
    """
    Algoritm recursiv pentru cautarea submultimilor de puncte coliniare
    """
    if i >= len(lista)-2:
        if len(print_list) > 2:
            print(print_list)
        return

    elif j >= len(lista)-1:
        i = i + 1
        j = i + 1
        k = j + 1

        if len(print_list) > 2: 
            print(print_list)

        print_list = [lista[i], lista[j]]
        rec(i, j, k, lista, print_list)

    elif k >= len(lista):
        if len(print_list) > 2:
            print(print_list)
        else:
            print("NU exista multimi")    

        j = j + 1
        k = j + 1

        print_list = [lista[i], lista[j]]
        rec(i, j, k, lista, print_list)



    else:
        a = lista[i]
        b = lista[j]
        c = lista[k]

        panta_ab = panta2(a, b)
        panta_bc = panta2(b, c)

        if panta_bc == panta_ab:
            print_list.append(c)
    
            if k==2:
                print(print_list)


        k = k + 1
        rec(i, j, k, lista, print_list)



recursiv()



#iterativ()