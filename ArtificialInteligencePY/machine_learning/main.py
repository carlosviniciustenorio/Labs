import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dados de exemplo
data = {
    'area': [50, 60, 100, 150, 200, 250, 300],
    'preco': [150, 180, 300, 450, 600, 750, 900]
}
df = pd.DataFrame(data)

# Separar variáveis
X = df[['area']]   # entrada
y = df['preco']    # saída

# Treinar modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

# Prever e visualizar
y_pred = model.predict(X_test)
print("Valores reais:", list(y_test))
print("Valores previstos:", list(y_pred))


plt.scatter(X_test, y_test, color='blue', label='Real')
plt.plot(X_test, y_pred, color='red', label='Previsão')
plt.xlabel('Área (m²)')
plt.ylabel('Preço (mil)')
plt.legend()
plt.show()