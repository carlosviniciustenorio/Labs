import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'area': [50, 60, 100, 150, 200, 250, 300],
    'preco': [150, 180, 300, 450, 600, 750, 900]
}

df = pd.DataFrame(data)

kmeans = KMeans(n_clusters=3, random_state=0)
print(kmeans)
df['cluster'] = kmeans.fit_predict(df[['area', 'preco']])

plt.scatter(df['area'], df['preco'], c=df['cluster'], cmap='viridis')
plt.xlabel('Área (m²)')
plt.ylabel('Preço (mil)')
plt.title('Clusters de imóveis')
plt.show()