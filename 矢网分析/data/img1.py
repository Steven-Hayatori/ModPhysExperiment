import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件中的表格
file_path = 'data.xlsx'
sheets = ['s11', 's12', 's21', 's22']
data = {sheet: pd.read_excel(file_path, sheet_name=sheet) for sheet in sheets}

# 创建一个2x2的子图布局
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()  # 将二维数组展平成一维，方便迭代

# 遍历每个表并绘制子图
for i, sheet_name in enumerate(sheets):
    df = data[sheet_name]
    ax = axes[i]
    
    # 绘制两条曲线，第一列为横坐标，第二、三列为纵坐标
    ax.plot(df.iloc[:, 0], df.iloc[:, 1], label=f'{sheet_name} - Real', color='blue')
    ax.plot(df.iloc[:, 0], df.iloc[:, 2], label=f'{sheet_name} - Imaginary', color='orange')
    
    # 设置子图标题和坐标标签
    ax.set_title(f'{sheet_name}')
    ax.set_xlabel('frequency f/Hz')
    ax.set_ylabel('parameter s/V')
    ax.legend()

# 设置整体图标题和布局调整
plt.suptitle('Origin Data')
plt.tight_layout(rect=[0, 0, 1, 0.96])  # 调整图形边距
plt.savefig('img1.png', dpi=300, bbox_inches='tight')
plt.show()

