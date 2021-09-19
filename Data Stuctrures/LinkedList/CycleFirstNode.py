def detectCycle(self, head):
    if not head:
        return 
    fast=slow=head
    pos=0
    node=None
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        pos+=1
        if fast==slow:
            node=fast
            break
    n=1
    while node:
        node=node.next
        if node==slow:
            break
        n+=1
    slow=fast=head
    while fast:
        while n:
            n-=1
            fast=fast.next
        if slow==fast:
            return slow
        if fast:
            fast=fast.next
            slow=slow.next
    return None
            
