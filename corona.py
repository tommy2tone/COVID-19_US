import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


style.use('ggplot')


df_confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')

df_usa_confirmed = df_confirmed[df_confirmed['Country/Region'] == 'US']

df_usa_confirmed = df_usa_confirmed.copy().drop(columns=['Lat', 'Long', 'Country/Region', 'Province/State'])\
                    .transpose().set_axis(['Confirmed'], axis=1)\
                    .reset_index().rename(columns={'index': 'Date'})
df_usa_confirmed['Date'] = pd.to_datetime(df_usa_confirmed['Date'])

df_usa_confirmed_daily = pd.DataFrame()

i = 1

for date, conf in df_usa_confirmed.iloc():
    # print('{} {}'.format(date, row))
    curr_index = i
    date_row = date
    conf_row = conf
    prev_index = i - 2
    previous_value = df_usa_confirmed.iloc[prev_index, 1]
    daily = conf_row - previous_value
    i += 1
    # print('{} {} {} {} {} {}'.format(date_row, curr_index, prev_index, conf_row, previous_value, daily))

    df_usa_confirmed_daily.at[date_row, 0] = daily

df_usa_confirmed_daily.set_axis(['Daily'], axis=1, inplace=True)
df_usa_confirmed_daily.reset_index(inplace=True)
df_usa_confirmed_daily.rename(columns={'index': 'Date'}, inplace=True)
df_usa_confirmed_daily['Date'] = pd.to_datetime(df_usa_confirmed_daily['Date'])
df_usa_confirmed_daily = df_usa_confirmed_daily[1:]

df_deaths = pd.read_csv('time_series_covid19_deaths_global.csv')

df_usa_deaths = df_deaths[df_deaths['Country/Region'] == 'US']

df_usa_deaths = df_usa_deaths.copy().drop(columns=['Lat', 'Long', 'Country/Region', 'Province/State'])\
                    .transpose().set_axis(['Deaths'], axis=1)\
                    .reset_index().rename(columns={'index': 'Date'})
df_usa_deaths['Date'] = pd.to_datetime(df_usa_deaths['Date'])

df_recovered = pd.read_csv('time_series_covid19_recovered_global.csv')

df_usa_recovered = df_recovered[df_recovered['Country/Region'] == 'US']

df_usa_recovered = df_usa_recovered.copy().drop(columns=['Lat', 'Long', 'Country/Region', 'Province/State'])\
                    .transpose().set_axis(['Recovered'], axis=1)\
                    .reset_index().rename(columns={'index': 'Date'})
df_usa_recovered['Date'] = pd.to_datetime(df_usa_recovered['Date'])
fig = plt.figure(figsize=(12, 8), frameon=True)

plt.title('USA Confirmed vs Deaths vs Recovered')
plt.xlabel('Dates')
plt.ylabel('Number of People')

ax = fig.add_subplot()
ax.plot(df_usa_confirmed['Date'], df_usa_confirmed['Confirmed'], label='Confirmed', linewidth=2)

ax.plot(df_usa_deaths['Date'], df_usa_deaths['Deaths'], label='Deaths', color='k', linewidth=2)

ax.plot(df_usa_recovered['Date'], df_usa_recovered['Recovered'], label='Recovered', linewidth=2)

ax.bar(df_usa_confirmed_daily['Date'], df_usa_confirmed_daily['Daily'], label='Daily Cases', color='y')

fig.legend(loc='upper left', borderaxespad=12)
plt.tight_layout()
plt.show()

