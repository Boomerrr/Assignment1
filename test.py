import matplotlib.pyplot as plt
import numpy as np

# x = [11422, 11360, 11312, 11274, 11233, 11196, 11160, 11129, 11098, 11038,
#      10984, 10944, 10903, 10863, 10828, 10789, 10752, 10715, 10675, 10639,
#      10654, 10619, 10587, 10550, 10510, 10466, 10425, 10389, 10350, 10311,
#      10272, 10237, 10196, 10161]
#
# y = [123, 120, 115, 110, 105, 100, 95, 90, 85, 80,
#      75, 70, 65, 60, 55, 50, 45, 40, 35, 30,
#      25, 20, 15, 10, 5, 0, -5, -10, -15, -20,
#      -25, -30, -35, -39.6]
# plt.plot(x, y, 'r-o')
# plt.plot(1, 2,'r-o',color="red")
# plt.plot(2, 1,'r-o',color="green")
# plt.show()


def find_lowest_cost_node(costs):
     lowest_cost = float("inf")
     lowest_cost_node = None
     for node in costs:  # 遍历所有节点
          cost = costs[node]
          if cost < lowest_cost and node not in processed:  # 如果当前节点的开销更低且未处理过
               lowest_cost = cost  # 将其视为开销最低的节点
               lowest_cost_node = node
     return lowest_cost_node


if __name__ == "__main__":
     # 构造有向赋权图 graph 存储所有节点的邻居
     graph = {}
     graph["start"] = {}  # 起点
     graph["start"]["a"] = 6
     graph["start"]["b"] = 2
     graph["a"] = {}  # a节点
     graph["a"]["final"] = 1
     graph["b"] = {}  # b节点
     graph["b"]["a"] = 3
     graph["b"]["final"] = 5
     graph["final"] = {}  # 终点没有任何邻居

     # 构造散列表costs 存储每个节点的开销
     # 节点的开销是指的从起点出发前往该节点需要多长时间
     # 对于还不知道的开销，你将其设置为无穷大
     infinity = float("inf")
     costs = {}
     costs["a"] = graph["start"]["a"]
     costs["b"] = graph["start"]["b"]
     costs["final"] = infinity

     # 还需要一个存储父节点的散列表
     parents = {}
     parents["a"] = "start"
     parents["b"] = "start"
     parents["final"] = None

     # 最后你需要一个数组，记录处理过的节点
     processed = []

     node = find_lowest_cost_node(costs)  # 找出开销最低的节点
     while node is not None:
          cost = costs[node]  # 获取该节点的开销
          neighbors = graph[node]  # 获取该节点的邻居 neighbors是一个散列表
          for n in neighbors.keys():  # 遍历邻居
               new_cost = cost + neighbors[n]
               if costs[n] > new_cost:  # 对新旧开销进行比较
                    costs[n] = new_cost
                    parents[n] = node
          processed.append(node)
          node = find_lowest_cost_node(costs)

     child = "final"
     parent = ["final"]
     while child != "start":
          parent.append(parents[child])
          child = parents[child]
          # print(parent)

     print("最短路径为：", parent[::-1])
     print("最短路径长度为：%d" % costs["final"])



