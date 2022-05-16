import matplotlib.pyplot as plt
import kode_awalan

fig, ax = plt.subplots(1, 1, figsize=(18, 9))
for device, group in kode_awalan.jenisDevices:
    group.mean = group.smoke.rolling(window=20).mean()
    ax.plot(group.mean,
            label=device)
fig.autofmt_xdate()
ax.grid()
ax.margins(0.05)
ax.legend()
plt.title('Perbandingan Asap Terhadap Waktu')
plt.ylabel('Banyak Asap')
plt.xlabel('Waktu')
plt.show()
