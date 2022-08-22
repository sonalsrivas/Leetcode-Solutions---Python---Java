# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        startHostName=re.findall(r"http://(\w*\.\w*\.\w*)[/.*]?", startUrl)[0]
        urlList=set([startUrl])
        q=deque()
        q.append(startUrl)
        while q:
            curUrl=q.popleft()
            urlsOnPage=htmlParser.getUrls(curUrl)
            for url in urlsOnPage:
                
                if startHostName in url and url not in urlList :
                    urlList.add(url)
                    q.append(url)
        return urlList