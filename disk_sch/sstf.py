requests = [95, 180, 34, 119, 11, 123, 62, 64]
head = 50


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


def sstf(head, requests):
    reqs = requests.copy()
    order = [head]
    current_head = head

    while reqs:
        # SSTF logic: find the request with minimum distance to current head
        closest = min(reqs, key=lambda x: abs(x - current_head))
        order.append(closest)
        reqs.remove(closest)
        current_head = closest

    seek = calculate_seek_time(order)
    return order, seek


# --- Execution ---
print("\n---------------------------------\n")
print(f"Initial Head Position: {head}")
print(f"Requests: {requests}")
print("\n---------------------------------\n")

order, seek = sstf(head, requests)

# Print visual path
print_disk_path(order)

print(f"Total Seek Time: {seek}")
print(f"Average Seek Time: {seek / len(requests):.2f}")
print("\n---------------------------------\n")
