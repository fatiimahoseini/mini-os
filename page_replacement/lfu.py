pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frames = 3


def print_memory_state(page, memory, fault, counts):
    status = "Fault" if fault else "Hit"
    # نمایش حافظه به همراه فرکانس هر صفحه برای درک بهتر استاد
    freq_str = {p: counts.get(p, 0) for p in memory}
    print(
        f"Page: {page:<2} | State: {status:<5} | Memory: {memory} | Freq: {freq_str}")


def lfu(pages, frames):
    memory = []
    count = {}
    page_fault = 0

    print("\n--- LFU Page Replacement Process ---")

    for page in pages:
        # افزایش فرکانس صفحه جاری
        count[page] = count.get(page, 0) + 1

        is_fault = False
        if page not in memory:
            is_fault = True
            page_fault += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                # پیدا کردن صفحه‌ای که کمترین فرکانس (LFU) را دارد
                least = min(memory, key=lambda x: count[x])
                memory.remove(least)
                memory.append(page)

        print_memory_state(page, memory, is_fault, count)

    return page_fault


# --- Execution ---
print(f"Total Pages: {pages}")
print(f"Frames: {frames}")

total_faults = lfu(pages, frames)

print("\n--------------------------")
print(f"Total Page Faults: {total_faults}")
print("--------------------------\n")
