from multiprocessing import Process
import multiprocessing
from typing import List



def digri_and_sum(number, digri):
    number_digri = number ** digri
    with open('result.txt', 'a+') as file:
        file.write(f'{number}^{digri}={number_digri} {sum_recurs(number_digri)}\n')


def sum_recurs(digri):
    sum = 0
    for i in range(digri):
        sum += i
    return sum


while True:
    i = 0
    while i < int(multiprocessing.cpu_count() / 2):
        try:
            string = input().split(' ')
            number = int(string[0])
            digri = int(string[1])
            list_process :List[Process] = []
            p = Process(target=digri_and_sum, args=(number, digri))
            p.start()
            list_process.append(p)
            i =+ 1
        except:
            print('ошибка')
    [process.join() for process in list_process]
