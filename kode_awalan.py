# maksud dari file kode awalan adalah kode yang akan dimasukkan kedalam kode lainnya
# saya menamai kode awalan karena kode ini mengawali setiap kode lainnya dengan cara mengimportnya ke file yang lain
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
