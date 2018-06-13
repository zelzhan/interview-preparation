// Implementation of vector (mutable array with automatic resizing)

#include <iostream>

using namespace std;

class ResizingVector{
  int length, cap;
  int *array;


public:

  //constructor
  ResizingVector(){
    length = 0, cap = 4;
    array = new int[cap];
  }

  //push the element to the end of the vector
  void push(int var){
    if (length == cap) {
      resize(2);
    }
    array[length] = var;
    length++;
  }


  // inserts item at index, shifts that index's value and trailing elements to the right
  void insert(int index, int item){
    if (index > length-1 || index < 0) {
      std::cout << "Error: Index out of range!" << '\n';
      return;
    }

    int *temp = new int[cap];
    for (int i = 0; i < length; i++) {
      temp[i] = array[i];
    }

    for (int j = 0, i = 0; j < length; j++, i++) {
      if (j == index) {
        array[j] = item;
        i++;
      }
      array[i] = temp[j];
    }
    length++;

    delete [] temp;
    temp = NULL;
  }

  //delete item at index, shifting all trailing elements left
  void del(int index){
    if (index > length-1 || index < 0) {
      std::cout << "Error: Index out of range!" << '\n';
      return;
    }

    int *temp = new int[cap];
    for (int i = 0; i < length; i++) {
      temp[i] = array[i];
    }

    int i = 0;
    for (int j = 0; j < length; j++, i++) {
      if (j == index) {
        j++;
      }
      array[i] = temp[j];
    }
    length--;
  }

  //remove the all instances of the element from the vector
  void remove(int item){
    for (int i = 0; i < length; i++) {
      if (array[i] == item) {
        del(i);
        i--;
      }
    }
  }

  //looks for value and returns first index with that value, -1 if not found
  int find(int item){
    for (int i = 0; i < length; i++) {
      if (array[i] == item) return i;
    }
    return -1;
  }

  //add item to the front of the vector
  void prepend(int item){
    insert(0, item);
  }

  //remove from front, return value
  int pop(){
    if (length == ((double)cap)/4) resize(1/2);
    array++;
    length--;
    return *(array-1);
  }

  //return the size of the vector
  int size(){
    return length;
  }

  //return the element at particular index
  int at(int index){
    if (index > length-1 || index < 0) {
      std::cout << "Error: Index out of range!" << '\n';
      return -1;
    }
    return array[index];
  }

  int capacity(){ return cap; }

  bool is_empty(){
    if (size() == 0) return true;
    return false;
  }

  //shows all elements of the vector
  void out(){
    for (int i = 0; i < length; i++) {
      std::cout << array[i] << '\n';
    }
  }


private:
  //helper for the push and pop methods
  //if argument is "2" increase the capacity of vector by the factor of 2
  //   otherwise cut the capacity by half
  void resize(double half){
    if (half == 2) {
      cap*=2;
      int *temp = new int[cap];
      for (int i = 0; i < cap/2; i++) {
        temp[i] = array[i];
      }
      delete [] array;
      array = temp;
      temp = NULL;

    } else {

      cap/=2;
      int *temp = new int[cap];
      for (int i = 0; i < cap; i++) {
        temp[i] = array[i];
      }
      delete [] array;
      array = temp;
      temp = NULL;
    }

  }

};

int main() {
  ResizingVector vec;
  vec.push(0);
  vec.push(2);
  vec.push(3);
  vec.push(2);
  vec.push(2);
  vec.push(3);
  vec.push(2);
  vec.push(2);
  vec.push(2);
  vec.pop();
  vec.pop();

  std::cout <<"CAPACITY IS " <<  vec.capacity() << '\n';
  std::cout << "The item is " << vec.find(3)<<'\n';

  vec.out();
}
