#  pip install matplotlib
#  pip install numpy

import matplotlib.pyplot as plt
import numpy as np

#  Valores do Grafico
y = np.array([35, 25, 25, 15])

#  Itens do Gráfico
mylabels = ['Platano', 'Maçâ', 'Uvas', 'Pera']

#  Espaço entre as Fatias do Grafico
myexplode = [0.2, 0, 0, 0]

#  Monta o Gráfico e depois mostra na tela
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()