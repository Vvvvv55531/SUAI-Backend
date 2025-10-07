#pragma once
#include <iostream>
using namespace std;

class Atr_Money // ����� ���������
{
public:
	long r; // ������������� ����������
	unsigned char k;

	Atr_Money() // ������������
	{
	};

	Atr_Money(long a, unsigned char b) : r(a), k(b)
	{
	};

	friend istream& operator>>(istream& input, Atr_Money& money); // ������������� �������
	friend ostream& operator<<(ostream& output, const Atr_Money& money);
};
