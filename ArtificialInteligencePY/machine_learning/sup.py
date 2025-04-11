import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    'area': [50, 60, 100, 150, 200, 250, 300],
    'preco': [150, 180, 300, 450, 600, 750, 900]
}
df = pd.DataFrame(data)

X = df[['area']]
y = df['preco']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.scatter(X_test, y_test, color='blue', label='Real')
plt.plot(X_test, y_pred, color='red', label='Previsão')
plt.xlabel('Área (m²)')
plt.ylabel('Preço (mil)')
plt.legend()
plt.show()