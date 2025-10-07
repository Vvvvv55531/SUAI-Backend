#pragma once
#include<iostream>
#include <string>
#include "Level_1.1.h"
#include "Level_1.2.h"
#include "Level_1.3.h"
using namespace std;

class Rocket : public Petrol, public Electricity, public Kerosene // наследование классов
{
private:
	string c3 = "at rest"; // инициализация переменных

public:
	Rocket(){} // кострукторы и деструкторы
	~Rocket(){cout << "destroying variables" << endl;}

	void Characteristic() override // инициализация методов
	{
		cout << "\nGeneral condition of transport:"
			<< "\ninternal combustion engine: "
			<< c1 << "\nelectric engine: " << c2 << "\nrocket engine: " << c4 << "\nrocket: " << c3 << endl;
	}
};
