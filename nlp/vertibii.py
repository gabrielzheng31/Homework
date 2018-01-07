

import numpy as np

# 模型参数
A = np.asarray([[0.7, 0.3], [0.4, 0.6]]) # 转移矩阵
B = np.asarray([[0.1, 0.4, 0.5], [0.6, 0.3, 0.1]])
Pi = np.asarray([0.6, 0.4]).transpose()

O = np.asarray([0,0,1,2]) 
T = O.shape[0]
N = A.shape[0]   # 状态数

p_nodes = Pi * B[:, O[0]]     # 记录每个节点的路径概率
path_nodes = list()           # 记录每个节点的路径
# 计初始化路径
for node in range(N):
    path_nodes.append([node])
# T 个时刻
for step in range(1, T):
    for this_node in range(N):   # 计算每个节点的新概率
        p_news = list()
        for last_node in range(N):
            p_trans = A[last_node, this_node]  # 转移概率
            p_out = B[this_node, O[step]]       # 输出概率
            p_new = p_nodes[last_node] * p_trans * p_out
            p_news.append(p_new)
        p_nodes[this_node] = np.max(p_news)    # 更新节点路径概率
        last_index = np.argmax(p_news)         # 更新节点路径
        temp = path_nodes[last_index][:]
        temp.append(this_node)
        path_nodes[this_node] = temp

print(p_nodes)     # 最有一步每个节点的概率
print(path_nodes) 
max_index = np.argmax(p_nodes)
max_path = path_nodes[max_index]
print(max_path)   # 最优路径
