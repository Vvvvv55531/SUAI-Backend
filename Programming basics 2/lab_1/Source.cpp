#include<iostream>
using namespace std;


double f11(double x1) // график прямой
{
	return x1;
}

double f12(double x2) // график 1 функции квадратного корня
{
	return sqrt(x2 + 2);
}

double f22(double x2) // график 2 функции квадратного корня
{
	return -sqrt(x2 + 2);
}

double tochki(double f1(double x2), double f2(double x2), double f3(double x1)) // точки пересечения
{
	f1 = f12;
	f2 = f22;
	f3 = f11;

	double x = 10000.0, y1 = f12(x), y2 = f22(x); // направление и вершина основной функции
	if (!((y1 >= 0.0) || (y2 <= 0.0)))
	{
		x = -x;
		y1 = f12(x);
		y2 = f22(x);
	}

	//cout << "- y1,2 for random +- x: " << x << y1 << y2 << endl;

	double v = (y1 + y2) / 2.0; // вершина Oy
	//cout << "- vershina for y: " << v << endl;

	double y, i = x / 10000.0, c = 1.0, a = 1.0, b, x1; // вершина Ox
	for (x1 = x; x1 != -x; x1 = (x1 - i) / c)
	{
		y = f12(x1);
		//if ((y == v) && (x1 == 0)) // случай, если Ox в нуле
		{
			//a = 0.0;
			//x1 = -x;
			//c = 1.0;
			//i = 0.0;
		}
		if (!((y >= 0.0) || (y <= 0.0)))
		{
			i = 0.0;
			c += 0.000000000001;
			cout << x1;

		}
		if ((((y >= 0.0) || (y <= 0.0)) && (i == 0.0)) && (a != 0.0))
		{
			c = 1.0;
			a = x1;
			x1 = -x;
		}
	}
	
	b = a;
	cout << "- vershina for x: " << a << x << endl; 
	b = round(b * 1000000.0) / 1000000.0; // округление результатов
	a = round(a * 1000000.0) / 1000000.0;

	i = x / 10000.0; // точка 1
	double  e = 0.0, z = 1.0;
	
	for (x1 = a + 0.1; x1 != x; x1 = (x1 + i) / c)
	{
		y1 = f22(x1);
		y2 = f11(x1);
		
		if ((y1 > y2) && (e != 1.0))
		{
			e = 2.0;
		}

		if ((y1 > y2) && (e != 2.0))
		{
			e = 1.0;
		}

		if (((y1 < y2) && (e == 2.0)) || ((y1 > y2) && (e == 1.0)))
		{
			c += 0.000000000001;
			i = 0.0;
			if ((x1 < 0) && (z == 1.0))
			{
				x1 = x1 - 0.00000001;
				c = 1.0;
				z == 2.0;
			}
		}

		if (((y1 > y2) && (i == 0.0) && (e == 2.0)) || ((y1 < y2) && (i == 0.0) && (e == 1.0)))
		{
			a = x1;
			v = y1;
			i = 0.0;
			c = 1.0;
			x1 = x;

		}
	}
	
	//cout << "- tochka 1: " << a << v << x << endl;

	i = x / 100000.0; e = 0.0;  //точка 2
	



	return 0;
}

int main()
{
	double x1, x2;
	cin >> x1 >> x2;

	f11(x1);
	f12(x2);
	f22(x2);

	//cout << "- y for x: " << f11(x1) << f12(x2) << f22(x2) << endl;
	tochki(f12, f22, f11);
	return 0;
}