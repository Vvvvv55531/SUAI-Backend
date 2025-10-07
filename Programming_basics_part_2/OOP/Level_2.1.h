#pragma once
#include<iostream>
#include <string>
#include "Level_1.1.h"
#include "Level_1.2.h"
using namespace std;

class Hybrid_car : public Petrol, public Electricity // наследование классов
{
private:
	string c3 = "wound up"; // инициализация переменных

public:
	Hybrid_car(){} // кострукторы и деструкторы
	~Hybrid_car(){cout << "destroying variables" << endl;}

	void Characteristic() override // инициализация методов
	{
		cout << "\nGeneral condition of transport:" 
		<< "\ninternal combustion engine: " 
		<< c1 << "\nelectric engine: " << c2 << "\ncar: " << c3 << endl;
	}
};
