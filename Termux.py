from selenium import webdriver
import time

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

print(rojo+"Se requiere un navegador Firefox!"+cierre)
time.sleep(2)
print (rojo+"Espere por favor"+cierre)
time.sleep(2)
print (blanco+"Cargando recursos , Gracias por usar mi script atte RIP")
time.sleep(1)
print (blanco+"[//    ]")
time.sleep(2)
print (blanco+"[///   ]")
time.sleep(2)
print (blanco+"[////  ]")
time.sleep(2)
print (blanco+"[///// ]")
time.sleep(2)
print (blanco+"[//////]")
time.sleep(2)


web = webdriver.Firefox()
web.get('https://piv.pivpiv.dk/')