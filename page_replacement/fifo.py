pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frames = 3


def print_memory_state(page, memory, fault):
    status = "Fault" if fault else "Hit"
    print(f"Page: {page:<2} | State: {status:<5} | Memory: {memory}")


def fifo(pages, frames):
    memory = []
    page_fault = 0

    print("\n--- FIFO Page Replacement Process ---")

    for page in pages:
        is_fault = False
        if page not in memory:
            is_fault = True
            page_fault += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)  # FIFO: Remove the oldest
                memory.append(page)

        print_memory_state(page, memory, is_fault)

    return page_fault


# --- Execution ---
print(f"Total Pages: {pages}")
print(f"Frames: {frames}")

total_faults = fifo(pages, frames)

print("\n--------------------------")
print(f"Total Page Faults: {total_faults}")
print("--------------------------\n")
