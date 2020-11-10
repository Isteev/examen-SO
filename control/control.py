from modelo.modelo import Modelo

print("ingresa el path")

path = "C:\\Users\\steev\\Desktop\\python\\prueba1.xlsx"

modelo = Modelo(path)

valor = "0"

while int(valor) < 10:
      print("1. ver toda la informacion\n"
            "2. promedio de temperaturas de entradas\n"
            "3. promedio de temperaturas de salida\n"
            "4. promdeio de temperatura en general\n"
            "5. promedio por persona\n"
            "6. temperatura mas alta de entrada\n"
            "7. temperatura mas alta de salida\n"
            "8. Graficar por fechas\n"
            "9. Todas las personas por fecha\n"
            "10. salir")

      valor = str(input())
      modelo.menu(valor)
      input()
