#include <cerrno>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

class fish {};

void win() {
  ifstream file("flag.txt");
  string flag;

  if (!file.is_open()) {
    cerr << "Failed to open \"flag.txt\"." << endl;
    exit(EXIT_FAILURE);
  }

  getline(file, flag);

  cout << "Oh! A Bite!" << endl;
  cout << "I caught the " << flag << " fish!" << endl;

  file.close();
  exit(EXIT_SUCCESS);
}

void first_try() {
  cout << "I'll try fishing here..." << endl;
  cout << "Hmm, doesn't seem like there are any fish to catch here." << endl;
  cout << endl;
}

void second_try() {
  char buf[32];
  fish s;

  cout << "Where should I try fishing instead?" << endl;
  cin.getline(buf, 512);
  cout << "Ok, I'll try fishing there..." << endl;
  cout << endl;

  // How does the program know which exception handler to use?
  // How is the return address significant?
  throw s;
}

int main() {
  try {
    cout << "I'm trying to catch the flag fish." << endl;
    cout << "Can you help me?" << endl;
    cout << endl;
    first_try();
  }
  catch (fish) {
    win();
  }

  try {
    second_try();
  }
  catch (fish) {
    cout << "Oh! A Bite!" << endl;
    cout << "Well it's not the flag fish I was looking for." << endl;
  }
}
