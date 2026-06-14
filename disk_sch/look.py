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
            # نشان دادن تغییر جهت حرکت با استفاده از علامت <->
            path += " --> "
    print(path)
    print("-----------------------------\n")


def look(head, requests):
    # LOOK logic: moves to the last request in the direction, then reverses
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    # Move right first, then reverse and move left
    order = [head] + right + left[::-1]

    seek = calculate_seek_time(order)
    return order, seek


# --- Execution ---
print("\n---------------------------------\n")
print(f"Initial Head Position: {head}")
print(f"Requests: {requests}")
print("\n---------------------------------\n")

order, seek = look(head, requests)

# Print visual path
print_disk_path(order)

print(f"Total Seek Time: {seek}")
print(f"Average Seek Time: {seek / len(requests):.2f}")
print("\n---------------------------------\n")
