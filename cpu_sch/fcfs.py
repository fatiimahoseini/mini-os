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


def fcfs(processes):
    processes = sorted(processes, key=lambda x: x["at"])
    time = 0
    for p in processes:
        if time < p["at"]:
            time = p["at"]
        start = time
        time += p["bt"]
        end = time
        gantt.append((p["name"], start, end))
    return gantt

# --- NEW FEATURE: VISUAL GANTT CHART ---


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
    print("\nAWT: ", awt)
    print("ATT: ", att)
    print("CPU Utilization: ", cpu, "%")


# Execution sequence
print("\n---------------------------------\n")
print("Process Table:")
print_process_table(processes)
print("\n---------------------------------\n")
print("Processes sequence in FCFS: ")
gantt_data = fcfs(processes)
print_gantt(gantt_data)

# Call the new feature
print_gantt_visual(gantt_data)

print("\n---------------------------------\n")
print_report(processes, gantt)
