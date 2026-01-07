from numpy import cov, var, min, max, sqrt, mean, std
import matplotlib.pyplot as plt

class RegressaoLinear:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def correlacao(self):
    covariacao = cov(self.x, self.y, bias=True)[0][1]
    variancia_x = var(self.x)
    variancia_y = var(self.y)

    return covariacao / sqrt(variancia_x * variancia_y)

  def inclinacao(self):
    stdx = std(self.x)
    stdy = std(self.y)

    return self.correlacao() * (stdy / stdx)

  def interceptacao(self):
    media_x = mean(self.x)
    media_y = mean(self.y)

    return media_y - media_x * self.inclinacao()
  
  def previsao(self, valor):
    return self.interceptacao() + self.inclinacao() * valor
  
  def PlotaRegressao(self, titulo='Regressao Linear', nome_x='Eixo X', nome_y='Eixo Y'):
    plt.xlabel(nome_x)
    plt.ylabel(nome_y)
    plt.title(titulo)

    plt.scatter(self.x, self.y)
    x_min = min(self.x)
    x_max = max(self.x)
    x_reta = [x_min, x_max]
    y_reta = [self.previsao(x_min), self.previsao(x_max)]
    plt.plot(x_reta, y_reta, color='red')
    plt.show()

idade = [18, 23, 25, 33, 34, 43, 48, 51, 58, 63, 67]
custo = [871, 1100, 1393, 1854, 1915, 2100, 2356, 2698, 2959, 3000, 3100]

regressao = RegressaoLinear(idade, custo)
prev = regressao.previsao(18)
print(prev)
regressao.PlotaRegressao('Plano de Saude', "Idade", "Custo")