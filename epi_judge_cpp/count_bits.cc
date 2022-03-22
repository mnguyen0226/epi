#include "test_framework/generic_test.h"
// 4/9/2021
// Prompt: Write a program to count the number of bits that are set to 1 in a nonnegative integer.
// Time Complexity: Best - O(1) to consider 1 bit; Worst - O(n) to consider n bits

short CountBits(unsigned int x) {
    //////////////////////////////////////////////////////////////// Way 1: brute force
     //Update the new number by shifting the current number 1 to the right
    int num_bit = 0; 
    // while the number of bit or x is not 0, then we stop considering
    while (x) {
        num_bit += x & 1; // Consider from the least significant bit
        x >>= 1; 
    }
    
  return num_bit;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "count_bits.cc", "count_bits.tsv", &CountBits,
                         DefaultComparator{}, param_names);
}
