import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('双探针.txt', delim_whitespace=True)

# 提取 Vo 和 I 的列
vo = data['Vo(V)']
current = data['I(uA)']

# 创建图表
plt.figure(figsize=(10, 6))

# 绘制折线图，设置线型、颜色、线宽和标记样式
plt.plot(vo, current, marker='o', linestyle='--', color='darkblue', linewidth=2, markersize=4, markerfacecolor='orange', markeredgewidth=1, markeredgecolor='black')

# 设置图表标题及横纵坐标标签
plt.title('Voltage vs Current', fontsize=16, fontweight='bold')
plt.xlabel('Voltage (Vo) [V]', fontsize=14)
plt.ylabel('Current (I) [uA]', fontsize=14)

# 设置坐标轴范围（可选，若需要固定范围）
plt.xlim(min(vo) - 0.1, max(vo) + 0.1)
plt.ylim(min(current) - 1, max(current) + 1)

# 设置网格线
plt.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# 美化坐标轴
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# 显示图表
plt.show()
