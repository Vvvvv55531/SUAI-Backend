#include<iostream>
using namespace std;

void draw_x(int);

int main()
{
	int a, b;
	cin >> a >> b;
	for (; a < b; a = a + 1)
		draw_x(a);
	return 0;
}

void draw_x(int size)
{
	for (int x = 0; x < size; x = x + 1)
	{
		for (int y = 0; y < (size * 3 - 2); y = y + 1)
		{
			if (y == -x + (size - 1) ||
				y == -x + (size * 3 - 3) ||
				y == x + (size - 1))
				cout << "#";
			else cout << ".";
		}
		cout << endl;
	}
}