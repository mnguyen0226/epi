/* 4/9/2021
 * The parity of a binary word is 1 is the number of 1s in the word is odd, otherwise 0.
 Parity checks are used to detect signle bit error in data storage and communication.
 => Compute the parity of a very large number of 64-bit words
 *
 */

#include "test_framework/generic_test.h"
short Parity(unsigned long long x) {
    //int one = 0;
    // while going thru that number
    //while (x) {
    //     if the bit is 1 then add to one
    //    one += x & 1;
    //    x >>= 1;
    //}
    // if number of 1s is odd then return 1
    //if (one % 2 == 1) {
    //    return 1;
    //
    //}
    //return 0;


    //////////////////////////////////////////////////////////////// Way 2: Reduce the time complexity way by counting only the number of 1s in the bits instead of keeping track of all the bit
    //int one = 0;
    //// while the number is not 0, then we stop
    //while (x) {
    //    // Ex: x = 0011 0010; x-1=0011 0000. Then x&(x-1) = 0011 0000 (this mean that there is still something in X)
    //    one += 1;
    //    x = x & (x - 1);
    //}
    //// if number of 1s is odd then return 1
    //if (one % 2 == 1) {
    //    return 1;

    //}
    //return 0;
    // Time complexity analysis, since way 2 method updates the current X by deleting the lowest 1 bit, then O(k) is the time complexity with k is number of 1s in the number

    /////////////////////////////////////////////////////////////// Way 3: Reduce the time complexity to O(logn) since the number of calculation reduce by 2 of the length of the number
    x ^= x >> 32;
    x ^= x >> 16;
    x ^= x >> 8;
    x ^= x >> 4;
    x ^= x >> 2;
    x ^= x >> 1;
    x &= 0x1;
    return x;

}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "parity.cc", "parity.tsv", &Parity,
                         DefaultComparator{}, param_names);
}
