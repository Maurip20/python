from statistics import linear_regression
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import numpy as np



df_midia = pd.read_csv(r"C:\Users\mauricio.santos\OneDrive - SERVICO SOCIAL DO COMERCIO-SESC\Mauricio\Cursos\Hashtag Treinamento - Python\Aula 4\advertising.csv")
print(df_midia)

# df_midia.info()
sns.heatmap(df_midia.corr(), cmap='Wistia', annot =True)
# plt.show()

x = df_midia.drop('Vendas', axis=1)
y = df_midia['Vendas']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3, random_state=1)


# Treinando modelo

lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

rf_reg = RandomForestRegressor()
rf_reg.fit = (x_train, y_train)

# Testando nossa IA

test_pred_lin = lin_reg.predict(x_test)
test_pred_rf = rf_reg.predict(x_test)

r2_lin = metrics.r2_score(y_test, test_pred_lin)
rmse_lin = np.sqrt(metrics.mean_squared_error(y_test,test_pred_lin))

print(f"R² da Regressão Linear: {r2_lin}")
print(f"RMSE da Regressão Linear: {rmse_lin}")

print("\n")
print("\n")
r2_rf= metrics.r2_score(y_test, test_pred_rf)
rmse_rf= np.sqrt(metrics.mean_squared_error(y_test, test_pred_rf))

print(f"R² da Regressão Linear: {r2_rf}")
print(f"RMSE da Regressão Linear: {rmse_rf}")


