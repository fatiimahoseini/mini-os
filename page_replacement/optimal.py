pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frames = 3


def print_memory_state(page, memory, fault):
    status = "Fault" if fault else "Hit"
    print(f"Page: {page:<2} | State: {status:<5} | Memory: {memory}")


def optimal(pages, frames):
    memory = []
    page_fault = 0

    print("\n--- Optimal Page Replacement Process ---")

    for i in range(len(pages)):
        page = pages[i]
        is_fault = False

        if page not in memory:
            is_fault = True
            page_fault += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                # پیدا کردن صفحه‌ای که در آینده دیرتر استفاده می‌شود
                farthest = -1
                remove_index = 0

                for j in range(len(memory)):
                    # بررسی می‌کنیم آیا صفحه در آینده وجود دارد یا خیر
                    try:
                        next_use = pages[i+1:].index(memory[j])
                    except ValueError:
                        # اگر دیگر استفاده نمی‌شود، بهترین گزینه برای حذف است
                        next_use = float('inf')

                    if next_use > farthest:
                        farthest = next_use
                        remove_index = j

                memory[remove_index] = page

        print_memory_state(page, memory, is_fault)

    return page_fault


# --- Execution ---
print(f"Total Pages: {pages}")
print(f"Frames: {frames}")

total_faults = optimal(pages, frames)

print("\n--------------------------")
print(f"Total Page Faults: {total_faults}")
print("--------------------------\n")
