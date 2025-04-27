import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        task_queue = []
        all_tasks = []

        for key, value in freq.items():
            heapq.heappush(task_queue, (value, key))
        
        while task_queue:
            pending_tasks = []
            batch_task = []
            for _ in range(len(freq)):
                if task_queue:
                    count, task = heapq.heappop(task_queue)
                    batch_task.append(task)

                    if count - 1 > 0:
                        pending_tasks.append((count-1, task))
                
            for pt in pending_tasks:
                heapq.heappush(task_queue, pt)

            while len(batch_task) < n+1 and task_queue:
                batch_task.append("IDLE")
            
            all_tasks = all_tasks + batch_task

        return len(all_tasks)