import functools
import math
from typing import Iterator, List, Tuple
import itertools
import heapq

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __lt__(self, rhs: "Star") -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


# 5/25/2022
# Because of the number of stars is too large, using the min-heap is in-efficient, we should use the max heap and get rid of the furthest one at a time
def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    # Put all the stars to the min-heap and retrieve the k number of stars
    results: List[Star] = []
    max_heap: List[Tuple[int, Star]] = []  # store the star and the distance

    # take the first k star
    for x in itertools.islice(stars, k):
        heapq.heappush(max_heap, (-x.distance, x))

    # add one star at the time, and get rid of the max
    for x in stars:
        _, _ = heapq.heappushpop(max_heap, (-x.distance, x))

    # after finish, add the star to the results
    while max_heap:
        _, furthest_star = heapq.heappop(
            max_heap
        )  # since we push negative, the pop is actually the pop the max out
        results.append(furthest_star)

    return results


# 5/25/2022
# Instead of using min heap to find the min in the set, we will use max heap as curated list
# This way is not useful for 10.2 because we not trying to find the smallest subset in the large dataset but to hand pick smallest one a t a time
def find_closest_k_stars_cleaner(stars: Iterator[Star], k: int) -> List[Star]:
    result: List[Star] = []
    max_heap: List[Tuple[int, Star]] = []

    # append new star until reach k + 1
    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))

        # get rid of the furthest star
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)

    # here, we got the curated list of closest stars
    while max_heap:
        _, star = heapq.heappop(max_heap)
        result.append(star)

    return result


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d) for s, d in zip(sorted(output), expected_output)
    )


# 6/10/2022
# We will use the max-heap to store k star and popout the furthest star until we go through the interator

import heapq


def find_closest_k_stars_2(stars: Iterator[Star], k: int) -> List[Star]:
    max_heap = []
    result = []

    # add the first k stars' distance to the max-heap
    for _ in range(k):
        star = next(stars, None)

        # calculate the distance
        if star is not None:
            dis = star.distance

            # add to max_heap
            heapq.heappush(max_heap, (-dis, star))

    # go through the array and push first then pop, else we will miss 1 stars
    while True:
        # get the next star
        next_star = next(stars, None)

        if next_star is not None:
            dis = next_star.distance
            heapq.heappushpop(max_heap, (-dis, next_star))
        else:
            break

    # collect the closest stars
    for tup in max_heap:
        result.append(tup[1])

    return result


# T: O(nlogk) with n is the size of stars, and k is the size of the heap
# S: O(logk) with k is the size of the heap


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars_2, iter(stars), k))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_closest_stars.py",
            "k_closest_stars.tsv",
            find_closest_k_stars_wrapper,
            comp,
        )
    )
