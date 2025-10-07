#include <iostream>
#include "Atr_Money.h"
#include "Money.h"

using namespace std;
int main() // вызов и проверка конструкторов и методов
{
	{Money n;
	cout << "0 arg\n";
	n.print(); }

	{Atr_Money m(97,27);
	Money n(m);
	cout << "Atr_Money class arg\n";
	n.print(); }

	{Money n(35);
	cout << "1 arg\n";
	n.print(); }

	{Money n(87,12);
	cout << "2 arg\n";
	n.print(); }

	cout << "deduction\n";
	(Money(25,5) - Money(2,1)).print();

	cout << "division\n";
	(Money(5,4) / Money(2,7)).print();
}
