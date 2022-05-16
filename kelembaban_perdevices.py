import matplotlib.pyplot as plt
import kode_awalan

fig, ax = plt.subplots(1, 1, figsize=(18, 9))
for device, group in kode_awalan.jenisDevices:
    group.mean = group.humidity.rolling(window=20).mean()
    ax.plot(group.mean,
            label=device)
fig.autofmt_xdate()
ax.grid()
ax.margins(0.05)
ax.legend()
plt.title('Perbandingan Kelembaban Terhadap Waktu')
plt.ylabel('Kelembaban (%)')
plt.xlabel('Waktu')
plt.show()
