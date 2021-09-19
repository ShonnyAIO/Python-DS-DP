def slidingSum(arr,k):
    if not arr or k==0:
        return
    queue=[]
    res=[]
    sum=0
    for i in range(len(arr)):
        if len(queue)==k:
            sum-=queue[0]
            queue.pop(0)
        queue.append(arr[i])
        sum+=arr[i]
        if len(queue)==k:
            res.append(sum)
    return res
