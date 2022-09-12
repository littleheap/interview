"""
lazy array: 要求实现 array.map(...).indexOf(...)，其中map传进去一个function,indexOf返回运行了所有function之后传入值的index。要求map的操作最后再做,所以叫lazy array

如果有多个map的call，这种情况要把多个function chain起来，所有的map的操作要delay到最后一步执行。

arr = LazyArray([10, 20, 30, 40, 50])
arr.map(lambda x:x*2).indexOf(40)  ----> 1
arr.map(lambda x:x*2).map(lambda x:x*3).indexOf(240) ----> 3 注意这里重新开了一个chain，上一行的map就不计算在内了
考虑缓存map和indexof的执行结果
 ---------
// lazy array，要求实现 array.map(...).indexOf(...)，其中map传进去一个function，
// indexOf返回运行了所有function之后传入值的index。要求map的操作最后再做，所以叫lazy array。For example:
// arr = LazyArray([10, 20, 30, 40, 50])
// arr.map(lambda x:x*2).indexOf(40)  ----> 1
// arr.map(lambda x:x*2).map(lambda x:x*3).indexOf(240) ----> 3 注意这里重新开了一个chain，上一行的map就不计算在内了
After finishing the implementation, asked about how to make class unit test friendly. And write unit test for the class.
Then ask how to improved the performance of lazyArray. My answer is using cache to store chain and correponding calculated value.
"""
