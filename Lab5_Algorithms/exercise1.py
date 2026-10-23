LAST_NAME = "Villamor"
STUDENT_ID = "TUPM-26-3469"
FAVORITE_ARTIST = "Steve Lacy"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(ord(c) - 64 for c in FAVORITE_ARTIST.upper() if c.isalpha())

print("LAST_NAME      :", LAST_NAME)
print("STUDENT_ID     :", STUDENT_ID)
print("FAVORITE_ARTIST:", FAVORITE_ARTIST)
print("SEED_DIGIT     :", SEED_DIGIT)
print("ID_SUM         :", ID_SUM)
print("NAME_LENGTH    :", NAME_LENGTH)
print("ARTIST_LENGTH  :", ARTIST_LENGTH)
print("ARTIST_SUM     :", ARTIST_SUM)


def linear_search(data, target):
    for i, value in enumerate(data):
        if value == target:
            return i, i + 1
    return -1, len(data)


def rotated_binary_search(data, target):
    low, high, comparisons = 0, len(data) - 1, 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if data[mid] == target:
            return mid, comparisons
        if data[low] <= data[mid]:
            if data[low] <= target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if data[mid] < target <= data[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1, comparisons


print("\n" + "=" * 60)
print("EXERCISE 1: EMERGENCY DISPATCH RECORD SEARCH")
print("=" * 60)

record_count = 15 + SEED_DIGIT
original = [100 + ID_SUM + i * (NAME_LENGTH + 1) for i in range(record_count)]
rotation_point = SEED_DIGIT % record_count
rotated = original[rotation_point:] + original[:rotation_point]

target_index = (ID_SUM + ARTIST_SUM) % record_count
target = original[target_index]
missing_target = target + 1

print("\nOriginal Dataset :", original)
print("Rotation Point   :", rotation_point)
print("Rotated Dataset  :", rotated)
print("Record Count     :", record_count)

print("\nTarget Incident  :", target)
rb_index, rb_comp = rotated_binary_search(rotated, target)
li_index, li_comp = linear_search(rotated, target)

print("\nRotated Binary Search -> position:", rb_index, "| comparisons:", rb_comp)
print("Linear Search         -> position:", li_index, "| comparisons:", li_comp)
print("Match Verified        :", rotated[rb_index] == target and rb_index == li_index)
print("Comparisons Saved     :", li_comp - rb_comp)

print("\nNot-Found Test (target =", missing_target, ")")
nb_index, nb_comp = rotated_binary_search(rotated, missing_target)
nl_index, nl_comp = linear_search(rotated, missing_target)
print("Rotated Binary Search -> position:", nb_index, "| comparisons:", nb_comp)
print("Linear Search         -> position:", nl_index, "| comparisons:", nl_comp)
print("Status                :", "Not found" if nb_index == -1 else "Found")

print("\nTIME AND SPACE COMPLEXITY")
print(f"{'Algorithm':<24}{'Time (Best)':<14}{'Time (Worst)':<16}{'Space':<8}")
print(f"{'Rotated Binary Search':<24}{'O(1)':<14}{'O(log n)':<16}{'O(1)':<8}")
print(f"{'Linear Search':<24}{'O(1)':<14}{'O(n)':<16}{'O(1)':<8}")

print("\nFINAL OUTPUT")
if rb_index != -1:
    print(f"Incident {target} found at position {rb_index} of the rotated list "
          f"using {rb_comp} comparisons (linear search: {li_comp}).")
else:
    print(f"Incident {target} not found after {rb_comp} comparisons.")