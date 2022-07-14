import matplotlib.pyplot as plt


x1 = [2,4,6,8]
y1 = [3,4,6,6]

x2 = [1,3,5,7]
y2 = [5,4,4,8]

titulo = "Comparação de dois gráficos em Python"
eixox = "Eixo X"
eixoy = "Eixo y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#plt.plot(x,y) - Método para plotar gráfico linear
plt.bar(x1,y1, label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")
plt.legend()

plt.show()