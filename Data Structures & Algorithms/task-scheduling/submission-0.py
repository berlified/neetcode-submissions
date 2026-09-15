class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)  #count for each tasks in dictionary.
        maxHeap = [-cnt for cnt in count.values()]      #convert all counts to -ve
        heapq.heapify(maxHeap)      #put it in a heap. #smallest actual values will be at the top.

        time = 0        #time counter for number of CPU intervals.
        q = deque()             #cool down. pairs of [-cnt, idleTime]
        while maxHeap or q:     #check whether we are still running the tasks,
            time += 1           

            if not maxHeap:
                time = q[0][1]          
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time