#pragma once
#include<iostream>
#include <string>
#include "Level 1.2.h"
#include "Level 1.3.h"
using namespace std;

class Plane : public Electricity, public Kerosene // наследование классов
{
private:
	string c3 = "on the ground"; // инициализация переменных

public:
	Plane(){} // кострукторы и деструкторы
	~Plane(){cout << "destroying variables" << endl;}

	void Сharacteristic() override // инициализация методов
	{
		cout << "\nGeneral condition of transport:"
			<< "\nelectric engine: " << c2 
			<< "\nrocket engine: " << c4 << "\nplane: " << c3 << "\n" << endl;
	}
};
