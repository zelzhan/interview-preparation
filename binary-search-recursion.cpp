#include <iostream>
#include <random>
#include <vector>

int binary_recursion(std::vector<int> vector, int target, int lo, int hi){

  //mid declaration
  int mid = lo + (hi-lo)/2;

  //if target not found
  if (hi < lo) return -1;

  //base case
  if (vector[mid] == target) return mid;
  if (vector[mid] > target) {
    return binary_recursion(vector, target, lo, mid-1);
  } else {
    return binary_recursion(vector, target, mid+1, hi);
  }
}



//test
int main() {
  std::vector<int> v(16);

  for (int i = 0; i < 15; i++) {
    v[i] = i;
    std::cout << "index " << i << " value " << i*i <<  '\n';
  }

  for (int i = 0; i < 15; i++) {
    std::cout << binary_recursion(v, i, 0, v.size()) << '\n';
  }

  std::cout << "Target " << binary_recursion(v, 1000, 0, v.size()) << '\n';

  return 0;
}
