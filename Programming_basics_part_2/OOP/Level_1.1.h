#pragma once
#include<iostream>
#include <string>
#include "Base_class.h"
using namespace std;

class Petrol : public Engine
{
public: 
	float Q1 = 3041; // инициализация переменных
	string c1 = "off";

public:
	Petrol(float q){Q = q;} // кострукторы и деструкторы
	Petrol(){};
	~Petrol(){cout << "destroying variables" << endl;}

	void Efficiency() // инициализация методов
	{
		cout << "efficiency: " << Q1 / Q << endl;
	}
	void Characteristic() override
	{
		cout << "condition: " << c1 << "\n" << endl;
	}
};
