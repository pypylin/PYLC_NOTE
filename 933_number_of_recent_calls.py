
class RecentCounter(object):

    def __init__(self):
        self.queue = []       

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        
        while len(self.queue) > 0 and self.queue[0] < t - 3000:
            del self.queue[0]
        self.queue.append(t)
        print len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(0)
param_1 = obj.ping(1)
param_1 = obj.ping(100)
param_1 = obj.ping(3005)
param_1 = obj.ping(6000)
param_1 = obj.ping(6005)
1, 99, 2900
