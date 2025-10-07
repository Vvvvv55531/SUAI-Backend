#pragma once
#include <iostream>
using namespace std;

class Atr_Money // класс атрибутов
{
public:
	long r; // инициализация переменных
	unsigned char k;

	Atr_Money() // конструкторы
	{
	};

	Atr_Money(long a, unsigned char b) : r(a), k(b)
	{
	};

	friend istream& operator>>(istream& input, Atr_Money& money); // дружественные функции
	friend ostream& operator<<(ostream& output, const Atr_Money& money);
};
