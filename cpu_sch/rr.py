from collections import deque
import matplotlib.pyplot as plt

processes = [
    {"name": "p1", "at": 0, "bt": 7, "priority": 2},
    {"name": "p2", "at": 2, "bt": 4, "priority": 1},
    {"name": "p3", "at": 4, "bt": 1, "priority": 3},
    {"name": "p4", "at": 5, "bt": 4, "priority": 2}
]
gantt = []


def print_process_table(processes):
    for p in processes:
        print(p)


def rr(processes, q=2):
    # Sort processes by arrival time
    sorted_processes = sorted(processes, key=lambda x: x["at"])
    queue = deque()
    time = 0
    i = 0
    remaining = {p["name"]: p["bt"] for p in sorted_processes}

    while i < len(sorted_processes) or queue:
        while i < len(sorted_processes) and sorted_processes[i]["at"] <= time:
            queue.append(sorted_processes[i]["name"])
            i += 1

        if not queue:
            time += 1
            continue

        name = queue.popleft()
        exec_time = min(q, remaining[name])

        start = time
        time += exec_time
        end = time

        gantt.append((name, start, end))
        remaining[name] -= exec_time

        while i < len(sorted_processes) and sorted_processes[i]["at"] <= time:
            queue.append(sorted_processes[i]["name"])
            i += 1

        if remaining[name] > 0:
            queue.append(name)
    return gantt

# --- VISUAL GANTT CHART FOR ROUND ROBIN ---


def print_gantt_visual(gantt):
    print("\n--- Visual Gantt Chart ---")
    bar = ""
    timeline = ""
    for g in gantt:
        bar += f"| {g[0]} "
        timeline += f"{g[1]:<4}"
    print(bar + "|")
    print(timeline + f"{gantt[-1][2]}")
    print("--------------------------\n")


def print_gantt(gantt):
    for g in gantt:
        print(g)


def calculate_metrics(processes, gantt):
    ct = {}
    for item in gantt:
        name, start, end = item
        ct[name] = end

    results = []
    total_wt = 0
    total_tat = 0

    for p in processes:
        name = p["name"]
        at = p["at"]
        bt = p["bt"]
        completion = ct[name]
        tat = completion - at
        wt = tat - bt
        total_wt += wt
        total_tat += tat
        results.append({"name": name, "AT": at, "BT": bt,
                       "CT": completion, "TAT": tat, "WT": wt})

    n = len(processes)
    avg_wt = total_wt / n
    avg_tat = total_tat / n
    total_time = max(ct.values())
    busy_time = sum([p["bt"] for p in processes])
    cpu_util = (busy_time / total_time) * 100
    return results, avg_wt, avg_tat, cpu_util


def print_report(processes, gantt):
    results, awt, att, cpu = calculate_metrics(processes, gantt)
    print("\nAWT: ", round(awt, 2))
    print("ATT: ", round(att, 2))
    print("CPU Utilization: ", round(cpu, 2), "%")


# --- Execution ---
print("\n---------------------------------\n")
print("Process Table:")
print_process_table(processes)
print("\n---------------------------------\n")
print("Processes sequence in Round Robin: ")

gantt_data = rr(processes)
print_gantt(gantt_data)
print_gantt_visual(gantt_data)

print("\n---------------------------------\n")
print_report(processes, gantt_data)
