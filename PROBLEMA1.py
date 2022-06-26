import pandas as pd

s=pd.Series([10,20,10])
r=pd.Series(['rojo','verde','azul'])

df=pd.Dataframe()
new_df=df.assign(s)
print(new_df)

nuev_df=df.assign(r)
print(nuev_df)

avengers=pd.read_csv('./src/pandas/avengers.csv')
print(avengers.head())

print('Las primeras 5 filas son:',avengers.head())
print('Las primeras 10 filas son:',avengers.head(10))
print('Las últimas 5 filas son:',avengers.tail())
print('El tamaño del dataframe llamado avenfers es:',avengers.size)
print('Los data types son:',avengers.dtypes)

m=avengers.set_index('fecha_inicio').copy()

n=m.sort_values(by=['fecha_inicio'],ascending=False)
print(n.head())

o=n.reset_index(drop=True, inplace=True)
print(o.head())
