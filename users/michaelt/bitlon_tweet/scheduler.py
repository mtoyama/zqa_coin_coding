import logging
from datetime import datetime, timedelta
from operator import itemgetter

LOGGER = logging.getLogger(__name__)

class Scheduler:
    def __init__(self):
        self.queue = []
    
    def register_task(self, func, params, delay, repeat=False):
        task_dict = {
            "func" : func,
            "params" : params,
            "delay": delay,
            "repeat": repeat
        }
        task_dict['execution_time'] = datetime.now() + timedelta(seconds=delay)

        self.queue.append(task_dict)
        
        # Sort the queue by execution time, which will save searching through
        # the entire queue to find tasks to execute. See check_and_run.
        self.queue = sorted(
            self.queue, key = itemgetter('execution_time'), reverse=False
        )

    def run_task(self, task_dict):
        LOGGER.info(f"Running task: {task_dict}")
        result = task_dict['func'](**task_dict['params'])
        if task_dict['repeat']:
            LOGGER.info("Task scheduled for repeat. Reschduling.")
            self.register_task(
                task_dict['func'],
                task_dict['params'],
                task_dict['delay'],
                task_dict['repeat']
            )
        return {'result': result, 'task_meta': task_dict}

    def check_and_run(self):
        results = []
        remove_tasks = []
        now = datetime.now()
        for task in self.queue:
            if task['execution_time'] <= now:
                results.append(self.run_task(task))
                self.queue.remove(task)
            else:
                break
        return results
