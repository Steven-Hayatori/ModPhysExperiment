import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取Excel文件中的表格
file_path = 'data.xlsx'
sheets = ['s11', 's12', 's21', 's22']
data = {sheet: pd.read_excel(file_path, sheet_name=sheet) for sheet in sheets}

# 计算 s11 和 s22 的平均值，s12 和 s21 的平均值
# 假设每个表格的第二列是实部，第三列是虚部
s11_avg_real = (data['s11'].iloc[:, 1] + data['s22'].iloc[:, 1]) / 2
s11_avg_imag = (data['s11'].iloc[:, 2] + data['s22'].iloc[:, 2]) / 2

s12_avg_real = (data['s12'].iloc[:, 1] + data['s21'].iloc[:, 1]) / 2
s12_avg_imag = (data['s12'].iloc[:, 2] + data['s21'].iloc[:, 2]) / 2

# 组合实部和虚部形成复数形式
s11_avg = s11_avg_real + 1j * s11_avg_imag
s12_avg = s12_avg_real + 1j * s12_avg_imag

# 提取频率列（假设频率列在第一列）
frequency = data['s11'].iloc[:, 0]  # 所有表的频率列相同

# 生成最终的表格：频率，s11 和 s12 的平均值（实部和虚部组合）
result_list = [[f, s11, s12] for f, s11, s12 in zip(frequency, s11_avg, s12_avg)]

miu_list = []
sigma_list = []
for i in result_list:
    f = i[0]
    s_11 = i[1]
    s_12 = i[2]
    lamda_0 = (3*(10**8)) / f
    lamda_c = 45.52 * 10**-3
    l = 1.9*10**-3

    K = (s_11**2 - s_12**2 + 1) / (2*s_11)
    GAMMA1 = np.abs(K + np.sqrt(K**2-1))
    GAMMA2 = np.abs(K - np.sqrt(K**2-1))
    GAMMA = GAMMA1 if GAMMA1 < 1 else GAMMA2
    T = s_12 / (1- GAMMA*s_11)
    
    delta2 = -(np.log((1/T)) / (2*np.pi*l))**2
    DELTA = np.sqrt(1/delta2)

    miu = ((1+GAMMA)/(1-GAMMA))  / (DELTA * np.sqrt((1/lamda_0**2 - 1/lamda_c**2)))
    miu_list.append(miu)
    sigma = (delta2 + 1/lamda_c**2) * (lamda_0**2) / miu
    sigma_list.append(sigma)

frequencies = [i[0] for i in result_list]  # 获取频率
miu_values = miu_list   # 获取 miu 值
sigma_values = sigma_list # 获取 sigma 值

# 创建一个包含四个子图的大图
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 第一个子图：f 与 miu 的实部和虚部的关系
ax1 = axes[0, 0]
ax1.plot(frequencies, np.real(miu_values), label="miu real part", color="blue", linestyle='-')
ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("miu Real Part")
ax1.set_title("f vs miu (Real and Imaginary Parts)")

# 创建右侧坐标轴来绘制 miu 的虚部
ax2 = ax1.twinx()
ax2.plot(frequencies, np.imag(miu_values), label="miu imaginary part", color="orange", linestyle='--')
ax2.set_ylabel("miu Imaginary Part")

# 绘制图例
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

# 第二个子图：f 与 sigma 的实部和虚部的关系
ax3 = axes[0, 1]
ax3.plot(frequencies, np.real(sigma_values), label="sigma real part", color="green", linestyle='-')
ax3.set_xlabel("Frequency (Hz)")
ax3.set_ylabel("sigma Real Part")
ax3.set_title("f vs sigma (Real and Imaginary Parts)")

# 创建右侧坐标轴来绘制 sigma 的虚部
ax4 = ax3.twinx()
ax4.plot(frequencies, np.imag(sigma_values), label="sigma imaginary part", color="red", linestyle='--')
ax4.set_ylabel("sigma Imaginary Part")

# 绘制图例
ax3.legend(loc="upper left")
ax4.legend(loc="upper right")

# 计算 miu 的幅值和角度
miu_magnitude = np.abs(miu_values)  # miu 的模
miu_phase = np.angle(miu_values)    # miu 的辐角

# 第三个子图：f 与 miu 的幅值和角度的关系
ax5 = axes[1, 0]
ax5.plot(frequencies, miu_magnitude, label="miu magnitude", color="blue", linestyle='-')
ax5.set_xlabel("Frequency (Hz)")
ax5.set_ylabel("miu Magnitude")
ax5.set_title("miu Magnitude and Phase")

# 创建右侧坐标轴来绘制 miu 的辐角
ax6 = ax5.twinx()
ax6.plot(frequencies, miu_phase, label="miu phase", color="orange", linestyle='--')
ax6.set_ylabel("miu Phase (radians)")

# 绘制图例
ax5.legend(loc="upper left")
ax6.legend(loc="upper right")

# 计算 sigma 的幅值和角度
sigma_magnitude = np.abs(sigma_values)  # sigma 的模
sigma_phase = np.angle(sigma_values)    # sigma 的辐角

# 第四个子图：f 与 sigma 的幅值和角度的关系
ax7 = axes[1, 1]
ax7.plot(frequencies, sigma_magnitude, label="sigma magnitude", color="green", linestyle='-')
ax7.set_xlabel("Frequency (Hz)")
ax7.set_ylabel("sigma Magnitude")
ax7.set_title("sigma Magnitude and Phase")

# 创建右侧坐标轴来绘制 sigma 的辐角
ax8 = ax7.twinx()
ax8.plot(frequencies, sigma_phase, label="sigma phase", color="red", linestyle='--')
ax8.set_ylabel("sigma Phase (radians)")

# 绘制图例
ax7.legend(loc="upper left")
ax8.legend(loc="upper right")

# 设置整体图的标题
plt.suptitle("Frequency vs miu and sigma (Real, Imaginary, Magnitude, and Phase)")

# 调整子图布局
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('img3.png', dpi=300, bbox_inches='tight')
# 显示图像
plt.show()
