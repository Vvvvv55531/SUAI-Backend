#pragma once
#include<iostream>
#include <string>
#include "Base_class.h"
using namespace std;

class Kerosene : public Engine
{
public: 
	unsigned char t = 360, hour = 3; // ������������� ����������
	string c4 = "broken";

public: 
	Kerosene(float a, float q){A = a; Q = q;} // ����������� � �����������
	Kerosene(){};
	~Kerosene(){cout << "destroying variables" << endl;}

	void Fuel_consumption() // ������������� �������
	{
		cout << "fuel consumption: " << hour / (A / t) << endl;
	}
	void �haracteristic() override
	{
		cout << "condition: " << c4 << "\n" << endl;
	}
};
