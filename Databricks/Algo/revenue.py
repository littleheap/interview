"""
revenue原题 然后有个follow up 是referral level 可以大于1

Customer Revenue系统，里面记录着每个customer产生的revenue，要你实现3个API：
1. insert(revenue): 一个新customer，产生了revenue，返回新customer的ID。customerID是自增ID，第一次insert是0，第二次是1，以此类推
2. insert(revenue, referrerID): 现有ID为referrerID的customer refer了一个新customer，产生了revenue，返回新customer的ID。
这种情况下认为referrer也产生了revenue。比如说customer 0之前产生的revenue为20，他refer了新人，产生了40revenue，customer 0产生的revenue就变为60
3. getKLowestRevenue(k, targetRevenue): 给定k和revenue，要求返回>给定revenue的k个最小revenue所对应的customer ID
4. complexity & edge cases

注意面试官可能要求你返回topk customer而不是top k revenue

问了两种storage方式，先说用topk经典pqueue存但面试官说换成更efficient就用了sortedlist

之后有一个follow up问要加一个给定 refer level=x 返回total revenue的api怎么写，直接写了个dfs/bfs就没时间了 不知道有没有更优的方法

前几问的时候是不是相当于refer level=1
这样做followup的时候怎么能算refer level=0呢 因为前几问存的data都是假设level=1
是的 会新存一个list来记录referral info 之后就对应的dfs/bfs就好了

Solution: treemap解

customer->revenue那个题，要实现referral api，最后get api是要求给一个customer id，return他的总的revenue，以及top k revenue。
"""