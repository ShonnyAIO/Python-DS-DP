def KFrequent(self, words: List[str], k: int) -> List[str]:
    m={}
    for word in words:
        if word not in m:
            m[word]=1
        else:
            m[word]+=1
    heap=[]
    for word in m:
        heapq.heappush(heap,(-m[word],word))
            
    res=[]
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res
