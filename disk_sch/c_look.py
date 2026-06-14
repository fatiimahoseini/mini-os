requests = [95, 180, 34, 119, 11, 123, 62, 64]
head = 50


def calculate_seek_time(order):
    seek = 0
    for i in range(1, len(order)):
        seek += abs(order[i] - order[i - 1])
    return seek

# --- NEW FEATURE: VISUAL DISK PATH ---


def print_disk_path(order):
    print("\n--- Visual Disk Head Path ---")
    path = ""
    for i in range(len(order)):
        path += f"[{order[i]}]"
        if i < len(order) - 1:
            path += " --> "
    print(path)
    print("-----------------------------\n")


def c_look(head, requests):
    # Separate requests into those greater and smaller than head
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    # C-LOOK logic: head moves to max right, jumps to min left, then continues
    order = [head] + right + left

    seek = calculate_seek_time(order)

    return order, seek


# --- Execution ---
print("\n---------------------------------\n")
print(f"Initial Head Position: {head}")
print(f"Requests: {requests}")
print("\n---------------------------------\n")

order, seek = c_look(head, requests)

# Print visual path
print_disk_path(order)

print(f"Total Seek Time: {seek}")
print(f"Average Seek Time: {seek / len(requests):.2f}")
print("\n---------------------------------\n")
