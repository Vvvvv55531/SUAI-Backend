#include "Money.h"
#include "Atr_Money.h"

Money::Money(long a, unsigned char b) // инициализация функций
{
	Money::money = Atr_Money(a, b);
};

Money::Money(Atr_Money n)
{
	Money::money = n;
};

Money::Money()
{
	Atr_Money n;
	std::cin >> n;
	Money::money = n;
};

void Money::print() {
	cout << money << '\n';
}