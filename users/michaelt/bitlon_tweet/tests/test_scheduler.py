import pytest
import time

from users.michaelt.bitlon_tweet import scheduler


def test_scheduler_basic():
    def task_func(test_param1, test_param2):
        return test_param1, test_param2

    schd = scheduler.Scheduler()
    schd.register_task(
        task_func,
        {"test_param1": 1, "test_param2": True},
        2
    )

    time.sleep(1)
    output = schd.check_and_run()
    assert len(output) == 0

    time.sleep(2)
    output = schd.check_and_run()
    assert output[0]['result'][0] == 1
    assert output[0]['result'][1] == True

def test_scheduler_multi():
    def task_func(test_param1, test_param2):
        return test_param1, test_param2

    schd = scheduler.Scheduler()
    schd.register_task(
        task_func,
        {"test_param1": 1, "test_param2": True},
        1
    )

    schd.register_task(
        task_func,
        {"test_param1": 2, "test_param2": False},
        2
    )

    time.sleep(1.5)
    print(schd.queue)
    output = schd.check_and_run()
    assert output[0]['result'][0] == 1
    assert output[0]['result'][1] == True

    time.sleep(1)
    output = schd.check_and_run()
    assert output[0]['result'][0] == 2
    assert output[0]['result'][1] == False