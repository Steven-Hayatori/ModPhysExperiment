import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件中的表格
file_path = 'data.xlsx'
sheets = ['s11', 's12', 's21', 's22']
data = {sheet: pd.read_excel(file_path, sheet_name=sheet) for sheet in sheets}

# 计算 s11 和 s22 的平均值，s12 和 s21 的平均值
avg_1 = (data['s11'] + data['s22']) / 2
avg_2 = (data['s12'] + data['s21']) / 2

# 创建 1x2 的子图布局
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 绘制第一个子图（s11 和 s22 的平均）
axes[0].plot(avg_1.iloc[:, 0], avg_1.iloc[:, 1], label='Avg - Real', color='blue')
axes[0].plot(avg_1.iloc[:, 0], avg_1.iloc[:, 2], label='Avg - Imaginary', color='orange')
axes[0].set_title('Average of s11 and s22')
axes[0].set_xlabel('frequency f/Hz')
axes[0].set_ylabel('parameter s/V')
axes[0].legend()

# 绘制第二个子图（s12 和 s21 的平均）
axes[1].plot(avg_2.iloc[:, 0], avg_2.iloc[:, 1], label='Avg - Real', color='blue')
axes[1].plot(avg_2.iloc[:, 0], avg_2.iloc[:, 2], label='Avg - Imaginary', color='orange')
axes[1].set_title('Average of s12 and s21')
axes[1].set_xlabel('frequency f/Hz')
axes[1].set_ylabel('parameter s/V')
axes[1].legend()

# 设置整体图标题和布局调整
plt.suptitle('Averaged Data')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('img2.png', dpi=300, bbox_inches='tight')
plt.show()