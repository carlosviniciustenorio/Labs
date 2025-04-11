import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'metros': [50, 60, 100, 150, 200, 250, 300],
    'preco': [150, 180, 300, 450, 600, 750, 900]
}
df = pd.DataFrame(data)

X = df[['metros']]
y = df['preco']

model = LinearRegression()
model.fit(X, y)

def prever_preco(metragem):
    preco_estimado = model.predict([[metragem]])[0]
    return round(preco_estimado, 2)

metragem_desejada = 350
print(f"Preço estimado para {metragem_desejada} m²: R$ {prever_preco(metragem_desejada)} mil")
