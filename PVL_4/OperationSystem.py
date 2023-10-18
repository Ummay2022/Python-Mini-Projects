from Process import Process

class OperationSystem:
    def __init__(self, kernel_number):
        self.kernel_number = kernel_number
        self.processes = []
        self.current_pid = 1

    def createProcess(self, arrival_time: int, execution_time: int, priority: int) -> int:
        pid = self.get_available_pid()
        if pid != -1:
            process = Process(pid, arrival_time, execution_time, priority)
            self.processes.append(process)
            return pid
        else:
            return -1

    def get_available_pid(self) -> int:
        while self.pid_exists(self.current_pid):
            if self.current_pid == 255:
                return -1
            self.current_pid += 1
        pid = self.current_pid
        self.current_pid += 1
        return pid

    def pid_exists(self, pid: int) -> bool:
        for process in self.processes:
            if process.get_pid() == pid:
                return True
        return False


    def deleteProcess(self, pid: int) -> bool:
        for process in self.processes:
            if process.get_pid() == pid:
                self.processes.remove(process)
                return True
        return False

    def execute(self) -> list[list[int]]:
        processors = [0] * self.kernel_number  # Initialize processors as idle (0)
        time = 0
        log = []

        while self.processes:
            current_processes = self.get_ready_processes(time)
            for i in range(self.kernel_number):
                if processors[i] == 0 and current_processes:
                    process = self.get_highest_priority_process(current_processes)
                    processors[i] = process.get_pid()
                    current_processes.remove(process)

            log.append(processors.copy())

            for i in range(self.kernel_number):
                if processors[i] != 0:
                    process = self.get_process_by_pid(processors[i])
                    process.execution_time -= 1
                    if process.execution_time == 0:
                        self.processes.remove(process)
                        processors[i] = 0

            time += 1

        return log

    def get_ready_processes(self, time: int) -> list[Process]:
        ready_processes = []
        for process in self.processes:
            if process.get_arrival_time() <= time:
                ready_processes.append(process)
        return ready_processes


    def get_highest_priority_process(self, processes: list[Process]) -> Process:
        highest_priority_process = processes[0]
        for process in processes:
            if process.get_priority() > highest_priority_process.get_priority():
                highest_priority_process = process
        return highest_priority_process


    def get_process_by_pid(self, pid: int) -> Process:
        for process in self.processes:
            if process.get_pid() == pid:
                return process
        return None










