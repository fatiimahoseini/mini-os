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
        # Highlight the boundary (end of disk)
        if order[i] == disk_size - 1:
            path += f"(*{order[i]}*)"
        else:
            path += f"[{order[i]}]"

        if i < len(order) - 1:
            path += " --> "
    print(path)
    print("-----------------------------\n")


def scan(head, requests, disk_size=200):
    # SCAN logic: Move to the end of the disk, then reverse
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    # Move to right end, then jump back left
    order = [head] + right + [disk_size - 1] + left[::-1]

    seek = calculate_seek_time(order)
    return order, seek


# --- Execution ---
print("\n---------------------------------\n")
print(f"Initial Head Position: {head}")
print(f"Requests: {requests}")
print("\n---------------------------------\n")

order, seek = scan(head, requests, disk_size)

# Print visual path
print_disk_path(order)

print(f"Total Seek Time: {seek}")
print(f"Average Seek Time: {seek / len(requests):.2f}")
print("\n---------------------------------\n")
