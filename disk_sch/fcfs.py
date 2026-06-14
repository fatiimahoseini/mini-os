requests = [95, 180, 34, 119, 11, 123, 62, 64]
head = 50
disk_size = 200


def calculate_seek_time(order):
    seek = 0
    for i in range(1, len(order)):
        seek += abs(order[i] - order[i - 1])
    return seek

# --- VISUAL DISK PATH ---


def print_disk_path(order):
    print("\n--- Visual Disk Head Path ---")
    path = ""
    for i in range(len(order)):
        path += f"[{order[i]}]"
        if i < len(order) - 1:
            path += " --> "
    print(path)
    print("-----------------------------\n")


def fcfs(head, requests):
    # FCFS logic: head visits requests in the exact order they arrive
    order = [head] + requests
    seek = calculate_seek_time(order)
    return order, seek


# --- Execution ---
print("\n---------------------------------\n")
print(f"Initial Head Position: {head}")
print(f"Requests: {requests}")
print("\n---------------------------------\n")

order, seek = fcfs(head, requests)

# Print visual path
print_disk_path(order)

print(f"Total Seek Time: {seek}")
print(f"Average Seek Time: {seek / len(requests):.2f}")
print("\n---------------------------------\n")
