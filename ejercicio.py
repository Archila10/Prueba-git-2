import matplotlib.pyplot as plt

#Datos de temperatura 
dias =list(range(1, 31))
temperaturas_ciudad_a = [22, 21, 23, 25, 24, 26, 27, 28, 29, 30, 31, 30, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]  
temperaturas_ciudad_b = [15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
temperatura_NY= [23, 20, 30, 15, 30, 23, 20, 16, 30, 16, 17, 18, 30, 27, 12, 29, 31, 20, 18, 20, 19, 17, 30, 20, 10, 18, 20, 30, 20, 21, 20, 12]

# Crear el gráfico​
plt.figure(figsize=(10, 5))

# Graficar las temperaturas​
plt.plot(dias, temperaturas_ciudad_a, label='Ciudad A', color='blue', linestyle='-', marker='o')
plt.plot(dias, temperaturas_ciudad_b, label='Ciudad B', color='red', linestyle='--', marker='x')
plt.plot(dias, temperatura_NY, label= 'temperatura_NY', color='green', linestyle= '-', marker= 'o' )

# Añadir título y etiquetas​
plt.title('Evolución de la Temperatura Diaria en tres Ciudades')
plt.xlabel('Día del Mes')
plt.ylabel('Temperatura (°C)')

# Añadir leyenda​
plt.legend()

# Mostrar el gráfico​
plt.grid(True)
plt.show()
