class Process:
    def __init__(self, pid, arrival_time, execution_time, priority):
        self.pid = pid 
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.priority = priority

    def get_pid(self) -> int:
        return self.pid

    def get_arrival_time(self) -> int:
        return self.arrival_time

    def get_execution_time(self) -> int:
        return self.execution_time

    def get_priority(self) -> int:
        return self.priority