import collections
#NAMEDTUPLE
semana=collections.namedtuple('semana',['lunes','martes','miercoles','jueves','viernes','sabado','domingo'])
Dias=semana(1,2,3,4,5,6,7)
print(Dias.martes)
