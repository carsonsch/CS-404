import random
import timeit

from binary_search import binary_search
from linear_search import linear_search

def generate_list_to_sort(length, should_be_sorted):
    lst = random.sample(range(0, 2_147_483_647), length)
    if should_be_sorted:
        lst.sort()
    return lst

def test_search_big_theta_linear(search_func, should_be_sorted):
    with open(search_func.__name__ + "_theta.csv", "wt", encoding="utf8") as csv_file:
        for i in range(1_000, 101_000, 1_000):

            runs = []
            for _ in range(0, 601):
                rand_lst = generate_list_to_sort(i, should_be_sorted)
                target = rand_lst[random.randint(0, i - 1)]
                speed_per_run = timeit.timeit(lambda: search_func(rand_lst, target), number=10) * 1000
                runs.append(speed_per_run)
            
            average_for_size = sum(runs) / len(runs)
            print(f"For i = {i}, {search_func.__name__}: {average_for_size}")
            csv_file.write(f"{i},{average_for_size}\n")

def test_search_big_o_linear(search_func, should_be_sorted):
    with open(search_func.__name__ + "_big_o.csv", "wt", encoding="utf8") as csv_file:
        for i in range(1_000, 100_000 * 300, 100_000):

            runs = []
            for _ in range(0, 101):
                rand_lst = generate_list_to_sort(i, should_be_sorted)
                target = 999999999999999
                rand_lst[i - 1] = target
                speed_per_run = timeit.timeit(lambda: search_asserter(search_func, rand_lst, target, i - 1), number=100) * 1000
                runs.append(speed_per_run)
            
            average_for_size = sum(runs) / len(runs)
            print(f"For i = {i}, {search_func.__name__}: {average_for_size}")
            csv_file.write(f"{i},{average_for_size}\n")

def test_search_big_o_binary(search_func, should_be_sorted):
    with open(search_func.__name__ + "_big_o.csv", "wt", encoding="utf8") as csv_file:
        for i in range(1, 26):

            arr_len = 2 ** i
            runs = []
            for _ in range(0, 101):
                rand_lst = generate_list_to_sort(arr_len, should_be_sorted)
                target = 999999999999999
                rand_lst[arr_len - 1] = target
                speed_per_run = timeit.timeit(lambda: search_asserter(search_func, rand_lst, target, arr_len - 1), number=100) * 100000
                runs.append(speed_per_run)
            
            average_for_size = sum(runs) / len(runs)
            print(f"For i = {arr_len}, {search_func.__name__}: {average_for_size}")
            csv_file.write(f"{arr_len},{average_for_size}\n")

def test_search_big_theta_binary(search_func, should_be_sorted):
    with open(search_func.__name__ + "_big_theta.csv", "wt", encoding="utf8") as csv_file:
        for i in range(1, 26):

            arr_len = 2 ** i
            runs = []
            for _ in range(0, 10001):
                rand_lst = generate_list_to_sort(arr_len, should_be_sorted)
                target_idx = random.randint(0, i - 1)
                target = rand_lst[target_idx]
                speed_per_run = timeit.timeit(lambda: search_asserter(search_func, rand_lst, target, target_idx), number=100) * 100000
                runs.append(speed_per_run)
            
            average_for_size = sum(runs) / len(runs)
            print(f"For i = {arr_len}, {search_func.__name__}: {average_for_size}")
            csv_file.write(f"{arr_len},{average_for_size}\n")

def test_search_big_omega_binary(search_func, should_be_sorted):
    with open(search_func.__name__ + "_big_omega.csv", "wt", encoding="utf8") as csv_file:
        for i in range(1, 26):

            arr_len = 2 ** i
            runs = []
            for _ in range(0, 101):
                rand_lst = generate_list_to_sort(arr_len, should_be_sorted)
                target_idx = (arr_len - 1) // 2
                target = rand_lst[target_idx]
                speed_per_run = timeit.timeit(lambda: search_asserter(search_func, rand_lst, target, target_idx), number=100) * 1000
                runs.append(speed_per_run)
            
            average_for_size = sum(runs) / len(runs)
            print(f"For i = {arr_len}, {search_func.__name__}: {average_for_size}")
            csv_file.write(f"{arr_len},{average_for_size}\n")

def test_search_big_omega_linear(search_func, should_be_sorted):
    with open(search_func.__name__ + "_big_omega.csv", "wt", encoding="utf8") as csv_file:
        for i in range(1_000, 101_000, 1_000):

            runs = []
            for _ in range(0, 101):
                rand_lst = generate_list_to_sort(i, should_be_sorted)
                target = 999999999999999
                rand_lst[0] = target
                speed_per_run = timeit.timeit(lambda: search_asserter(search_func, rand_lst, target, 0), number=100) * 1000
                runs.append(speed_per_run)
            
            average_for_size = sum(runs) / len(runs)
            print(f"For i = {i}, {search_func.__name__}: {average_for_size}")
            csv_file.write(f"{i},{average_for_size}\n")

def search_asserter(search_func, lst, target, expected_pos):
    pos = search_func(lst, target)
    assert pos == expected_pos

test_search_big_o_binary(binary_search, True)
test_search_big_omega_binary(binary_search, True)
test_search_big_theta_binary(binary_search, True)

test_search_big_o_linear(linear_search, False)
test_search_big_theta_linear(linear_search, False)
test_search_big_omega_linear(linear_search, False)
