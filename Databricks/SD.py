"""
1. Design the VISA payment system.
2. Design a stock buy/sell exchange system , Given REST API for undering stock transaction execution system.
3. Design WebCrawler: First write single threaded Web Crawler, Then write multi-threaded WebCrawler.

    一开始提供了三个utility function：
    (1)fetch(URL: url) -> HTML: content;
    (2)parse(HTML: content) -> List<URL>;
    (3)save(URL: url, HTML: content)。
    `save`是把数据存在disk上，`fetch`是发个network request，`parse`是in-memory解析html page，

    Improve the efficiency by multi-thread
    1 - avoid race condition where two threads check same url and try to process as next url at same time (this causes duplicate visit on same url)
    use concurrentHashMap put to avoid, since the put (insert entry) lock the segment of map and if return null meaning no such key in map previously which means we can process the url
    2 - save is a disk I/O where we should put it into a separate thread pool to let it finish by itself
    3 - fetch html is a network I/O
4.
"""