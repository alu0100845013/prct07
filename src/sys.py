import modulo
l=[]
def mostrar(l):
t_upla=(10,100,1000,10000,100000,1000000,10000000,100000000)
for i in range(0,len(t_upla)):
  ap= modulo.aprox(t_upla[i])
#print l
mostrar (l)
# el maximo numero de elementos de la t-upla es de 8
# para 9 o mas elementos
# no es posible
#cuando el programador importa un modulo tambien crea una version compilada y ya tiene extension .pyc