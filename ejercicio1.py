angulo1=-1
angulo2=-1
while(angulo1<0)or(angulo1>180):
    angulo1=int(input("Ingrese el primer angulo: "))
while(angulo2<0)or(angulo2>180):
    angulo2=int(input("Ingrese el segundo angulo: "))

if(angulo1+angulo2==180):
    print("Son suplementarios")
else:
    print("No son suplementarios")