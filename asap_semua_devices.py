import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# perintah untuk membuat data frame dari data csv yang telah disediakan
frameData = pd.read_csv('iot_telemetry_data.csv')
# ini adalah program untuk menampilkan jumlah data pada terminal
jumlahdata = frameData["smoke"].index
print("jumlah data = ", len(jumlahdata))
# sma adalah singkatan dari Simple Moving Average artinya mengambil data rata-rata setiap beberapa kali input data. agar data yang tak beraturan seperti yang ada pada data raw asap menjadi lebih mulus dan dapat dengan mudah dianalisis. pada kodingan ini, saya membuat datanya dirata-rata setiap 1000 kali setiap pengambilan data.
frameData['SMA_1000_asap'] = frameData["smoke"].rolling(
    1000, min_periods=1).mean()
# ini adalah perintah untuk memploting data untuk asap, sma asap, dan ploting data lainnya
plt.plot(frameData["smoke"])
plt.plot(frameData['SMA_1000_asap'])
# melabeli sumbu x dan y
plt.xlabel("data ke-")
plt.ylabel("nilai data")
# membuat legend untuk setiap garis data
plt.legend(["data asap", "data asap SMA_1000_asap"])
# judul grafik
plt.title("ploting data sensor")
# menampilkan grafik pada layar
plt.show()
