"""
You are given N randomly generated connected graphs. Write an algorithm to merge them into a single randomly connected graph with the smallest number of edges possible.

uniform distribution指的是所有nodes from input有edge的概率一样大

Input: a list of graphs.

Output: the collection of new edges added.

Solution:
randomly select 2 graphs and remove them
randomly select one node from each of 2 graphs
connect the two nodes to get one connected graph
add the connected graph back to graphs list
repeat until number of graphs is 1
"""