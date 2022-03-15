from time import perf_counter_ns
import simples as sp
import mtrhead as mt

with open("data.csv") as file:
    data = [line.strip() for line in file]

data = list(map(int, data))

print('\n\nanalise de %d valores\n\n'%(len(data)))

for threads in range(5):

    simple_time_array = []

    thread_time_array = []

    for i in range(50):
        start1 = perf_counter_ns()
        prime_sp = sp.resolve_simples(data)
        finish1 = perf_counter_ns()
        simple_time = (finish1-start1)/1000000
        simple_time_array.append(simple_time)

        start2 = perf_counter_ns()
        prime_mt = mt.resolve_trhread(data, threads+1)
        finish2 = perf_counter_ns()
        thread_time = (finish2-start2)/1000000
        thread_time_array.append(thread_time)

    all_simple_times = 0

    all_thread_times = 0

    for i in range(50):
        all_simple_times += simple_time
        all_thread_times += thread_time


    average_simple_time = all_simple_times/len(simple_time_array)
    average_thread_time = all_thread_times/len(thread_time_array)

    SpeedUp = average_simple_time/average_thread_time
    
    if (average_simple_time > average_thread_time):
        print('simples          > threads (%d)'%(threads))
        print('%f ms   > %f ms  : tempo execucao'%(average_simple_time,average_thread_time))
        print('%d            > %d           :numeros primos encontrados\n'%(prime_sp,prime_mt))
        print('SpeedUp =', SpeedUp)
        print()