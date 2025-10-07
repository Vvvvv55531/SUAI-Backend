#include<iostream>
#include <cmath> 
using namespace std;


double cos_a(double x1, double x2, double x3, double
	y1, double y2, double y3)
{
	double a1, a2, b1, b2, ab, a, b, ygol;
	a1 = x2 - x1;
	a2 = y2 - y1;
	b1 = x2 - x3;
	b2 = y2 - y3;
	a = pow(a1 * a1 + a2 * a2, 0.5);
	b = pow(b1 * b1 + b2 * b2, 0.5);
	ab = a1 * b1 + a2 * b2;
	ygol = acos(ab / (a * b));
	ygol = ygol / 0.0175;
	return ygol;
}
int main()
{
	double x1, x2, x3, y1, y2, y3, ygol;
	int n = 0;
	cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
	for (int i = 0; i < 3; i++) 
	{
		ygol = cos_a(x1, x2, x3, y1, y2, y3);
		if (ygol < 90.0)
			n += 1;
		double t;
		t = x1;
		x1 = x2;
		x2 = x3;
		x3 = t;
		t = y1;
		y1 = y2;
		y2 = y3;
		y3 = t;
	}
	cout << n;
	return 0;
}


