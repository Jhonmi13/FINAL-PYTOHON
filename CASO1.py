import pandas as pd
df_airbnb = pd.read_csv("./src/pandas/airbnb.csv")

df_airbnb.head()
df_airbnb[(df_airbnb.reviews>10)&(df_airbnb.overall_satisfaction>4)]

n=df_airbnb.sort_values(by=['overall_satisfaction','reviews'],ascending=[False,False])
print(n.head(3))