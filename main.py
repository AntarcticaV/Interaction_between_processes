from multiprocessing import Process
import multiprocessing as mp
import multiprocessing
from typing import List



def digri_and_sum(queue :mp.Queue()):
    number = queue.get()
    digri = queue.get()
    number_digri = number ** digri
    with open('result.txt', 'a+') as file:
        file.write(f'{number}^{digri}={number_digri} {sum_recurs(number_digri)}\n')


def sum_recurs(digri):
    sum = 0
    for i in range(digri):
        sum += i
    return sum


queue = mp.Queue()
while True:
    try:
        string = input().split(' ')
        queue.put(int(string[0]))
        queue.put(int(string[1]))
    except:
        print('ошибка')
        queue.get()
        queue.get()
    list_process = []
    for i in range(int(queue.qsize() / 2)):
        # сделать очереди
        work = mp.Process(target=digri_and_sum, args=(queue))
        work.start()
        list_process.append(work)
    [process.join() for process in list_process]
    
    