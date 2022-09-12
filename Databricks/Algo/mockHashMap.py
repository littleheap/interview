"""
设计一个mockHashMap的class，其中包含这几个API：
put(key, val)
get(key)
messure_put_load()
messure_get_load()
其中put和get就和普通hashmap一样，messure方法需要返回
average times per second that put/get function be called within past 5 minutes，就是当前时间的‍前五分钟内，
平均每秒钟put/get 被调用的次数
After the coding, ask to how make the class unit test friendly, how to simulate testing requests in last 5 minutes or anytime period. And write unit test.
"""