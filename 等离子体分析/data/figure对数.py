import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('单探针CD.txt', delim_whitespace=True)

# 提取 Vo 和 I 的列
vo = data['Vo(V)']
current = data['I(uA)']
delta_I = np.log(current[10]/(10**6)) - np.log(current[5]/(10**6))
delta_V = vo[10] - vo[5]
slope = delta_I / delta_V
print(f"第一个点处的斜率为: {slope:.4f} A/V")
# 创建半对数图表
plt.figure(figsize=(10, 6))

# 使用半对数绘制折线图，y轴使用log刻度
plt.semilogy(vo, current, marker='o', linestyle='--', color='darkblue', linewidth=2, 
             markersize=8, markerfacecolor='orange', markeredgewidth=1, markeredgecolor='black')

# 设置图表标题及横纵坐标标签
plt.title('Voltage vs Current (Semilog Plot)', fontsize=16, fontweight='bold')
plt.xlabel('Voltage (Vo) [V]', fontsize=14)
plt.ylabel('Current (I) [uA] (Log Scale)', fontsize=14)

# 设置坐标轴范围（可选，根据数据情况进行调整）
plt.xlim(min(vo) - 0.1, max(vo) + 0.1)

# 美化网格线，调整y轴为对数网格
plt.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# 美化坐标轴刻度
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# 显示图表
plt.show()
