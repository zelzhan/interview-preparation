#include <iostream>

using namespace std;

class ResizingVector{
  int length, cap;
  int *array;


public:
  ResizingVector(){
    length = 0;
    cap = 4;
    array = new int[cap];
  }

  void push(int var){

    if (length == cap) {
      resize(2);
    }
    array[length] = var;
    // counter++;
    length++;
  }

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

  void remove(int item){
    for (int i = 0; i < length; i++) {
      if (array[i] == item) {
        del(i);
        i--;
      }
    }
  }

  int find(int item){
    for (int i = 0; i < length; i++) {
      if (array[i] == item) {
        return i;
      }
    }
    return -1;
  }

  void prepend(int item){
    insert(0, item);
  }

  int pop(){
    if (length == ((double)cap)/4) {
      resize(1/2);
    }
    array++;
    length--;
    return *(array-1);
  }

  int size(){
    return length;
  }

  int at(int index){
    if (index > length-1 || index < 0) {
      std::cout << "Error: Index out of range!" << '\n';
      return -1;
    }
    return array[index];
  }

  int capacity(){
    return cap;
  }

  bool is_empty(){
    if (array == NULL) {
      return true;
    }
    return false;
  }

  void out(){
    for (int i = 0; i < length; i++) {
      std::cout << array[i] << '\n';
    }
  }
private:
  void resize(double half){
    if (half == 2) {
      int *temp = new int[cap];
      for (int i = 0; i < cap; i++) {
        temp[i] = array[i];
      }
      cap*=2;
      array = new int[cap];
      for (int j = 0; j < cap; j++) {
        array[j] = temp[j];
      }

      delete [] temp;
      temp = NULL;
    } else {
      int *temp = new int[cap];
      for (int i = 0; i < cap; i++) {
        temp[i] = array[i];
      }
      cap/=2;
      array = new int[cap];
      for (int j = 0; j < cap; j++) {
        array[j] = temp[j];
      }

      delete [] temp;
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

  vec.out();
}
