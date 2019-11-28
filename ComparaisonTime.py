import time 
f=np.sin
a=-5
b=5
n_=int(input("n? (les polynômes seront de degré 2n+1)"))
debutLT=time.time()
n=2*n_+2
racines=[(a+b)/2+(a-b)/2*np.cos((2*k+1)*(np.pi)/(2*n)) for k in range(0,n)]
ycoords=[f(x) for x in racines]
L=polynome_Lagrange(racines,ycoords)
finLT=time.time()
dureeLT=finLT-debutLT
debutLH=time.time()
n_=n_+1
racines=[(a+b)/2+(a-b)/2*np.cos((2*k+1)*(np.pi)/(2*n)) for k in range(0,n)]
ycoords=[f(x) for x in racines]
dycoords=[misc.derivative(f,x) for x in racines]
L=polynome_lhermite(racines,ycoords,dycoords)
finLH=time.time()
dureeLH=finLH-debutLH
debutSP=time.time()
liste=[]
xcoords=[a+k*(b-a)/n for k in range(n+1)]
ycoords=[f(k) for k in xcoords]    
dycoords=[misc.derivative(f,k) for k in xcoords]    
for k in range(n):
        a0=ycoords[k+1]/(xcoords[k+1]-xcoords[k])
        a1=ycoords[k]/(xcoords[k]-xcoords[k+1])
        a2=(dycoords[k]-a0-a1)/((xcoords[k]-xcoords[k+1])**2)
        a3=(dycoords[k+1]-a0-a1)/((xcoords[k+1]-xcoords[k])**2)
        nu0=-a0*xcoords[k]-a1*xcoords[k+1]-a2*xcoords[k]*xcoords[k+1]**2-a3*xcoords[k]**2*xcoords[k+1]
        nu1=a0+a1+a2*(xcoords[k+1]**2+2*xcoords[k+1]*xcoords[k])+a3*(xcoords[k]**2+2*xcoords[k]*xcoords[k+1])
        nu2=-a2*(xcoords[k]+2*xcoords[k+1])-a3*(xcoords[k+1]+2*xcoords[k])
        nu3=a2+a3
        P=[nu0,nu1,nu2,nu3]
        liste.append(P)
finSP=time.time()
dureeSP=finSP-debutSP
debutSE=time.time()
L=serie_entiere(f,n)
finSE=time.time()
dureeSE=finSE-debutSE
print("-> durée de Lagrange:",dureeLH)
print("-> durée de L'Hermite:",dureeLT)
print("-> durée des splines:",dureeSP)
print("-> durée des séries entières",dureeSE)