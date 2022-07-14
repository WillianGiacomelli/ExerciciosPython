import matplotlib.pyplot as plt


x = [1,2,5]
y = [3,4,6]
titulo = "Gráfico em Python"
eixox = "Eixo X"
eixoy = "Eixo y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#plt.plot(x,y) - Método para plotar gráfico linear
plt.bar(x,y)
plt.show()