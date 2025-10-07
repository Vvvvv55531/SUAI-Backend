#pragma once
#include<iostream>
#include <string>
#include "Base_class.h"
using namespace std;

class Kerosene : public Engine
{
public: 
	unsigned char t = 360, hour = 3; // инициализация переменных
	string c4 = "broken";

public: 
	Kerosene(float a, float q){A = a; Q = q;} // кострукторы и деструкторы
	Kerosene(){};
	~Kerosene(){cout << "destroying variables" << endl;}

	void Fuel_consumption() // инициализация методов
	{
		cout << "fuel consumption: " << hour / (A / t) << endl;
	}
	void Characteristic() override
	{
		cout << "condition: " << c4 << "\n" << endl;
	}
};
