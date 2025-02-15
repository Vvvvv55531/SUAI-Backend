#pragma once
#include <iostream>
#include <string>
#include "Atr_Money.h"
using namespace std;

class Money
{
private:
	Atr_Money money; // класс атрибутов

public:
	Money(long a, unsigned char b = 0); // конструкторы
	Money(Atr_Money n);
	Money();

	Money operator - (const Money& m) const // методы задания
	{
		long r1 = money.r * 100 + money.k;
		long r2 = m.money.r * 100 + m.money.k;
		long r = abs(r1 - r2) / 100;
		long k = abs(r1 - r2) % 100;

		return Money(r,k);
	}
	Money operator / (const Money& m) const
	{
		long r1 = money.r * 100 + money.k;
		long r2 = m.money.r * 100 + m.money.k;
		long r = (r1/r2) / 100;
		long k = (r1/r2) % 100;

		return Money(k,r);
	}
	void print();
};
