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


def sjf(processes):
    processes = processes.copy()
    time = 0
    completed = []

    while processes:
        available = [p for p in processes if p["at"] <= time]

        if not available:
            time += 1
            continue

        p = min(available, key=lambda x: x["bt"])
        processes.remove(p)

        start = time
        time += p["bt"]
        end = time

        gantt.append((p["name"], start, end))

    return gantt


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

        results.append({
            "name": name,
            "AT": at,
            "BT": bt,
            "CT": completion,
            "TAT": tat,
            "WT": wt
        })

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


print("\n---------------------------------\n")
print("Proccess Table:")
print_process_table(processes)
print("\n---------------------------------\n")
print("Processes sequence in SJF: ")
print_gantt(sjf(processes))
print("\n---------------------------------\n")
print_report(processes, gantt)
