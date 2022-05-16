import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# konversi ke datetime


def parse(x):
    return pd.to_datetime(x, infer_datetime_format=True, unit='s', utc=True)


# perintah untuk membuat data frame dari data csv yang telah disediakan. disini saya membaca hanya sampai 100.000 data saja agar komputer saya cepat menghitung datanya :)
frameData = pd.read_csv('iot_telemetry_data.csv', nrows=100000, index_col=[
                        'ts'], infer_datetime_format=True, date_parser=parse)
# gunakan kode dibawah kalau ingin menampilkan semua datanya (total ada 405184 row data wkwkwk)
# frameData = pd.read_csv('iot_telemetry_data.csv')
# ini adalah program untuk menampilkan jumlah data pada terminal
jumlahdata = frameData["humidity"].index
print("jumlah data = ", len(jumlahdata))
# perintah untuk mensorting data
df = frameData.sort_values(by='ts', ascending=True)
# mempreview data yang telah dimanipulasi sebelumnya
print(df.head(5))
jenisDevices = df.groupby('device')
# jumlah data per devices
print('Record count:\n{}'.format(jenisDevices.size()))
# perintah untuk memploting data dengan sumbu x adalah temperatur dan sumbu y adalah kelembaban
_, ax = plt.subplots(1, 1, figsize=(18, 9))
for device, group in jenisDevices:
    ax.plot(group.temp,
            group.humidity,
            marker='o',
            linestyle='',
            alpha=.5,
            ms=10,
            label=device)
ax.grid()
ax.margins(0.05)
ax.legend()
plt.title('Temperatur vs. Humidity')
# hanya mengira2 dalam derajat celcius karena suhu ruangan dalam celcius rata2 memang segitu :)
plt.xlabel('Temperatur (˚C)')
plt.ylabel('kelembaban (%)')
plt.show()
