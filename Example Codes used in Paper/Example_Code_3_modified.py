def odd_count(lst):
    return sorted([i for i in lst if all(int(c) % 2 == 1 for c in str(i)) and i > 10])