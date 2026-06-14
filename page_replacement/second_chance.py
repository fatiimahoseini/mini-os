pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frames = 3


def print_memory_state(page, memory, fault, refs):
    status = "Fault" if fault else "Hit"
    # نمایش وضعیت حافظه و بیت‌های ارجاع کنار آن
    ref_map = dict(zip(memory, refs))
    print(
        f"Page: {page:<2} | State: {status:<5} | Memory: {memory} | RefBits: {ref_map}")


def second_chance(pages, frames):
    memory = []
    reference = []
    pointer = 0
    page_fault = 0

    print("\n--- Second Chance Page Replacement Process ---")

    for page in pages:
        is_fault = False
        if page in memory:
            # Hit: صفحه پیدا شد، بیت ارجاع آن را ۱ می‌کنیم
            index = memory.index(page)
            reference[index] = 1
        else:
            # Fault: صفحه در حافظه نیست
            is_fault = True
            page_fault += 1

            if len(memory) < frames:
                memory.append(page)
                reference.append(1)
            else:
                # جستجو برای صفحه‌ای که بیت ارجاع آن ۰ است (شانس دوم)
                while True:
                    if reference[pointer] == 0:
                        memory[pointer] = page
                        reference[pointer] = 1
                        pointer = (pointer + 1) % frames
                        break
                    else:
                        reference[pointer] = 0
                        pointer = (pointer + 1) % frames

        print_memory_state(page, memory, is_fault, reference)

    return page_fault


# --- Execution ---
print(f"Total Pages: {pages}")
print(f"Frames: {frames}")

total_faults = second_chance(pages, frames)

print("\n--------------------------")
print(f"Total Page Faults: {total_faults}")
print("--------------------------\n")
