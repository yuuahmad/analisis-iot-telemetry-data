import matplotlib.pyplot as plt
import kode_awalan

# perintah untuk memploting data dengan sumbu x adalah temperatur dan sumbu y adalah kelembaban
_, ax = plt.subplots(1, 1, figsize=(18, 9))
for device, group in kode_awalan.jenisDevices:
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
# dari data yang ditampilkan, bisa disimpulkan kalau:
# device 00:0f:00:70:91:0a berada pada kondisi yang dingin dan sangat lembab
# device b8:27:eb:bf:9d:51 berada pada kondisi yang hangat dan kelembaban yang cenderung kering
# device 1c:bf:ce:15:ec:4d berada dalam kondisi temperatur dan kelembaban yang tidak stabil
