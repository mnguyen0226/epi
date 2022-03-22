# 3/10/2022
# Problem Statement: Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
# This is easy if you use O(n) space, where n is the length of the array. However, you are required to solve it without allocating additional storage

# Solution 1: Make a copy of input array, go though O(n) and insert
# Time Complexity: O(n)
# Space Complexity: O(n)
def sort_even(a):
    sorted_a = []
    for i in range(len(a)):
        if a[i] % 2 == 0:  # make copy of even number first
            sorted_a.append(a[i])
    for i in range(len(a)):
        if a[i] % 2 == 1:  # then make copy of odd numer
            sorted_a.append(a[i])
    return sorted_a


# Solution 2: Choose two ends, if the left end is even, then increment left index, else, swap with other number then decrease right index
# Time Complexity: O(n)
# Space Complexity: O(n)
def sort_even_2(a):
    even_idx, odd_idx = 0, len(a) - 1
    while even_idx < odd_idx:
        if a[even_idx] % 2 == 0:
            even_idx += 1
        else:
            a[even_idx], a[odd_idx] = a[odd_idx], a[even_idx] # this mean run two operation at the same time
            odd_idx -= 1
    return a


def main():
    print("Running")
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    new_a = sort_even_2(a)
    print(new_a)


if __name__ == "__main__":
    main()
