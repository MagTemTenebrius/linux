import sys
import os
import time
from typing import Tuple, Optional, List

import psutil

log_file = './file.log'
G_PID = os.getpid()


def validate_command(argv: List[str]) -> Tuple[bool, Optional[str], Optional[int], Optional[int]]:
    """
    Функция валидации переданных аргументов
    :param argv: список аргументов
    :return: верна ли комбинация параметров, сообщение процесса, количество процессов, количество итераций
    """
    if len(argv) < 7:
        return False, None, None, None
    return True, argv[argv.index('-m') + 1], int(argv[argv.index('-p') + 1]), int(argv[argv.index('-n') + 1])


def fork_process(process_count: int, iteration_count: int, message: str) -> List[int]:
    """
    Функция форка
    :param process_count: количество форков
    :param iteration_count: число итераций
    :param message: сообщение
    :return: список процессов-воркеров
    """
    workers = []
    try:
        for process in range(process_count):
            print(f'P {os.getpid()}: fork {process}')
            worker_pid = os.fork()
            if not worker_pid:
                now = time.time()
                for j in range(iteration_count * (process + 1)):
                    with open(log_file, mode='a+') as file:
                        file.write(f'[C] {now}: {message} {j + 1}\n')
                    time.sleep(1)
                    if not psutil.pid_exists(G_PID):
                        os.abort()
                os.abort()
            workers.append(worker_pid)
    except:
        for i in workers:
            os.kill(i, 0)
    return workers


def main():
    validate, message, processes, iterations = validate_command(sys.argv)
    if not validate:
        print('main.py -m <message>, -p <process_count> -n <iteration_count>')
        return

    workers = fork_process(processes, iterations, message)

    for pid in workers:
        print(f'[P] Waiting for {pid}')
        os.waitpid(pid, 0)


if __name__ == "__main__":
    main()
