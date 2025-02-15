#include <iostream>

using namespace std;

int expon(int a, int b) {
	int count = 1;
	int i = 0;
	while (i < b)
	{
		count *= a + 1;
		i++;
	}

	return count;
}

int main() {
	cout << expon(2, 3);

	return 0;
}
