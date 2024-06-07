import pandas as pd
from datetime import datetime, timedelta

cdata1 = pd.read_csv('imported_by_China_17-18.csv', header=10, nrows=15)
cdata2 = pd.read_csv('imported_by_China_18-19.csv', header=10, nrows=15)
cdata3 = pd.read_csv('imported_by_China_19-20.csv', header=10, nrows=15)
cdata4 = pd.read_csv('imported_by_China_20-21.csv', header=10, nrows=15)
cdata5 = pd.read_csv('imported_by_China_21-22.csv', header=10, nrows=15)
cdata6 = pd.read_csv('imported_by_China_22-23.csv', header=10, nrows=15)
cdata7 = pd.read_csv('imported_by_China_23-24.csv', header=10, nrows=15)

udata1 = pd.read_csv('imported_by_United_States_of_America_17-18.csv', header=10, nrows=15)
udata2 = pd.read_csv('imported_by_United_States_of_America_18-19.csv', header=10, nrows=15)
udata3 = pd.read_csv('imported_by_United_States_of_America_19-20.csv', header=10, nrows=15)
udata4 = pd.read_csv('imported_by_United_States_of_America_20-21.csv', header=10, nrows=15)
udata5 = pd.read_csv('imported_by_United_States_of_America_21-22.csv', header=10, nrows=15)
udata6 = pd.read_csv('imported_by_United_States_of_America_22-23.csv', header=10, nrows=15)
udata7 = pd.read_csv('imported_by_United_States_of_America_23-24.csv', header=10, nrows=15)

country_name = input("Enter the country name: ")
year = input("Enter the year (e.g., 2018): ")
month = input("Enter the month (e.g., 10): ")
input_date = datetime.strptime(f"{year}-{month}", "%Y-%m")
previous_month = input_date - timedelta(days=input_date.day)
time1 = f'Imported value in {year}-M{month}'
time2 = f'Imported value in {previous_month.year}-M{previous_month.month:02d}'

if datetime(2017, 11, 1) <= input_date <= datetime(2018, 9, 30):
    cdata = cdata1
    udata = udata1
elif datetime(2018, 10, 1) <= input_date <= datetime(2019, 8, 31):
    cdata = cdata2
    udata = udata2
elif datetime(2019, 9, 1) <= input_date <= datetime(2020, 7, 31):
    cdata = cdata3
    udata = udata3
elif datetime(2020, 8, 1) <= input_date <= datetime(2021, 6, 30):
    cdata = cdata4
    udata = udata4
elif datetime(2021, 7, 1) <= input_date <= datetime(2022, 5, 31):
    cdata = cdata5
    udata = udata5
elif datetime(2022, 6, 1) <= input_date <= datetime(2023, 4, 30):
    cdata = cdata6
    udata = udata6
elif datetime(2023, 5, 1) <= input_date <= datetime(2024, 3, 31):
    cdata = cdata7
    udata = udata7
else:
    cdata = None

if not cdata.empty:
    df1 = pd.DataFrame(cdata)
    value1 = df1.loc[df1['Exporters'] == country_name, time1].values[0]
    value2 = df1.loc[df1['Exporters'] == country_name, time2].values[0]
    ratio1 = value1/value2
    formatted_ratio1 = "{:.2f}".format(ratio1)
else:
    print("No data available for the given date range.")

if not udata.empty:
    df2 = pd.DataFrame(udata)
    value3 = df2.loc[df2['Exporters'] == country_name, time1].values[0]
    value4 = df2.loc[df2['Exporters'] == country_name, time2].values[0]
    ratio2 = value3/value4
    formatted_ratio2 = "{:.2f}".format(ratio2)
else:
    print("No data available for the given date range.")

if formatted_ratio1 > formatted_ratio2:
    winner = "china"
else:
    winner = "USA"

print(f"Imported by China: {value1}")
print(f"Increased ratio by China: {formatted_ratio1}")
print(f"Imported by USA: {value3}")
print(f"increased ratio by USA: {formatted_ratio2}")
print(f"prefered country = {winner}")


