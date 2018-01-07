# -*- coding: utf-8 -*-

import networkx as nx

import matplotlib.pyplot as plt

class PRIterator:
    __doc__ = '''计算一张图中的PR值'''

    def __init__(self, dg):
        self.damping_factor = 0.85  # 阻尼系数,即α
        self.max_iterations = 100  # 最大迭代次数
        self.min_delta = 0.00001  # 确定迭代是否结束的参数,即ϵ
        self.graph = dg

    def page_rank(self):
        #  先将图中没有出链的节点改为对所有节点都有出链
        for node in self.graph.nodes():
            if len([*self.graph.neighbors(node)]) == 0:
                for node2 in self.graph.nodes():
                    self.graph.add_edge(node, node2)

        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # 给每个节点赋予初始的PR值
        damping_value = (1.0 - self.damping_factor) / graph_size  # 公式中的(1−α)/N部分

        flag = False
        count = 0
        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for in_edge in self.graph.in_edges(node):  # 遍历所有“入射”的页面
                    if node == in_edge[0]:
                        incident_page = in_edge[1]
                    else:
                        incident_page = in_edge[0]
                    rank += self.damping_factor * (page_rank[incident_page] / len([*self.graph.neighbors(incident_page)]))
                rank += damping_value
                change += abs(page_rank[node] - rank)  # 绝对值
                page_rank[node] = rank

            print("This is NO.%s iteration" % (i + 1))
            print(page_rank)

            if change < self.min_delta:
                flag = True
                count = i
                break
        print()
        if flag:
            print("finished in %s iterations!" % count)
        else:
            print("finished out of 100 iterations!")
        return page_rank


if __name__ == '__main__':
    dg = nx.gnm_random_graph(10, 40, directed=True)
    nx.draw(dg, with_labels=True)
    plt.show()

    pr = PRIterator(dg)
    page_ranks = pr.page_rank()

    print("The final page rank is\n", page_ranks)
