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
        # Highlight boundary points (0 and 199) for clarity
        if order[i] == 0 or order[i] == disk_size - 1:
            path += f"(*{order[i]}*)"
        else:
            path += f"[{order[i]}]"

        if i < len(order) - 1:
            path += " --> "
    print(path)
    print("-----------------------------\n")


def c_scan(head, requests, disk_size=200):
    # Separate requests
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    # C-SCAN logic: moves to end, jumps to 0, then continues
    order = [head] + right + [disk_size - 1, 0] + left

    seek = calculate_seek_time(order)
    return order, seek


# --- Execution ---
print("\n---------------------------------\n")
print(f"Initial Head Position: {head}")
print(f"Requests: {requests}")
print("\n---------------------------------\n")

order, seek = c_scan(head, requests, disk_size)

# Print visual path
print_disk_path(order)

print(f"Total Seek Time: {seek}")
print(f"Average Seek Time: {seek / len(requests):.2f}")
print("\n---------------------------------\n")
