def FCFS(processes):
    processes.sort(key=lambda x: x[0])  # Sort by arrival time
    start_time = 0
    gantt_chart = []
    waiting_times = []
    turnaround_times = []
    
    for arrival_time, burst_time in processes:
        waiting_time = start_time - arrival_time
        turnaround_time = waiting_time + burst_time
        waiting_times.append(waiting_time)
        turnaround_times.append(turnaround_time)
        gantt_chart.append((start_time, start_time + burst_time))
        start_time += burst_time
    
    return {
        "gantt_chart": gantt_chart,
        "waiting_times": waiting_times,
        "turnaround_times": turnaround_times
    }

def SJF(processes):
    processes.sort(key=lambda x: (x[0], x[1]))  # Sort by arrival time, then burst time
    start_time = 0
    gantt_chart = []
    waiting_times = []
    turnaround_times = []
    
    for arrival_time, burst_time in processes:
        waiting_time = start_time - arrival_time
        turnaround_time = waiting_time + burst_time
        waiting_times.append(waiting_time)
        turnaround_times.append(turnaround_time)
        gantt_chart.append((start_time, start_time + burst_time))
        start_time += burst_time
    
    return {
        "gantt_chart": gantt_chart,
        "waiting_times": waiting_times,
        "turnaround_times": turnaround_times
    }

def RoundRobin(processes, time_quantum):
    from collections import deque
    
    queue = deque(processes)
    start_time = 0
    gantt_chart = []
    waiting_times = []
    turnaround_times = []
    remaining_burst_times = {p: bt for p, bt in processes}
    
    while queue:
        arrival_time, burst_time = queue.popleft()
        if remaining_burst_times[(arrival_time, burst_time)] > time_quantum:
            remaining_burst_times[(arrival_time, burst_time)] -= time_quantum
            gantt_chart.append((start_time, start_time + time_quantum))
            start_time += time_quantum
            queue.append((arrival_time, burst_time))  # Re-add to queue
        else:
            gantt_chart.append((start_time, start_time + remaining_burst_times[(arrival_time, burst_time)]))
            start_time += remaining_burst_times[(arrival_time, burst_time)]
            remaining_burst_times[(arrival_time, burst_time)] = 0
            
    return {
        "gantt_chart": gantt_chart,
        "waiting_times": waiting_times,
        "turnaround_times": turnaround_times
    }
