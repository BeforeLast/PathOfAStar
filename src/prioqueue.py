PRIORITY_INDEX = 0

class PriorityQueue :
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    # enqueue tuple to self.queue
    # input :
    #   tuple : tup
    # I.S. : [..]
    # F.S. : [..,tup]
    # !! IMPORTANT : tup[0] must be a number as a priority that can be compared !!
    def enqueue(self, tup):
        if len(self.queue) == 0:
            self.queue.append(tup)
        else:
            for i in range(len(self.queue)):
                if self.queue[i][PRIORITY_INDEX] >= tup[0]:
                    self.queue.insert(i,tup)
                    return
            self.queue.insert(len(self.queue),tup)

    # dequeue self.queue
    # I.S. : [front,..]
    # F.S. : [..]
    # output : tuple
    def dequeue(self):
        if len(self.queue) == 0:
            return []
        tup = self.queue[0]
        self.queue = self.queue[1:]
        return tup

if __name__ == '__main__':
    prioQueue = PriorityQueue()

    tup1 = (1,"A")
    tup2 = (3,"C")
    tup3 = (2,"D")
    tup4 = (1,"B")

    prioQueue.enqueue(tup1)
    prioQueue.enqueue(tup2)
    prioQueue.enqueue(tup3)
    prioQueue.enqueue(tup4)

    print(prioQueue.queue)