from typing import Union, final
from datetime import timedelta
import functools
import time
import json


class Benchmark(object):
    n: Union[int, timedelta] = timedelta(seconds=5)
    sample: int = 10
    warmup: Union[int, timedelta] = timedelta(seconds=1)
    timer = time.perf_counter

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @final
    def measure(self) -> timedelta:
        begin = self.timer()
        # TODO call function
        end = self.timer()

        return end - begin
