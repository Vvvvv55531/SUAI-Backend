#pragma once
#include<iostream>
#include <string>
#include "Base_class.h"
using namespace std;

class Petrol : public Engine
{
public: 
	float Q1 = 3041; // ������������� ����������
	string c1 = "off";

public:
	Petrol(float q){Q = q;} // ����������� � �����������
	Petrol(){};
	~Petrol(){cout << "destroying variables" << endl;}

	void Efficiency() // ������������� �������
	{
		cout << "efficiency: " << Q1 / Q << endl;
	}
	void �haracteristic() override
	{
		cout << "condition: " << c1 << "\n" << endl;
	}
};
