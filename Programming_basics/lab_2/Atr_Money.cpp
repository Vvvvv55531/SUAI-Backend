#include "Atr_Money.h"

std::istream& operator>>(istream& input, Atr_Money& money) // ����
{
	cout << "RUB/KOP\n";
	input >> money.r; // ������� �� char � int
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

std::ostream& operator<<(ostream& output, const Atr_Money& money) // �����
{
	int i = static_cast<int>(money.k);
	output << money.r << "," << i;
	return output;
}
