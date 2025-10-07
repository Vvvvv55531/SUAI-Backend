#include "Atr_Money.h"

std::istream& operator>>(istream& input, Atr_Money& money) // ввод
{
	cout << "RUB/KOP\n";
	input >> money.r; // перевод из char в int
	input >> money.k;
	int i = static_cast<int>(money.k);
	while ((money.r < 0) || (money.k < 0) || (money.k >= 100))
	{
		cout << "Incorrect value, enter another!\n";
		input >> money.r;
		input >> money.k;
		int i = static_cast<int>(money.k);
	}
	return input;
}

std::ostream& operator<<(ostream& output, const Atr_Money& money) // вывод
{
	int i = static_cast<int>(money.k);
	output << money.r << "," << i;
	return output;
}
