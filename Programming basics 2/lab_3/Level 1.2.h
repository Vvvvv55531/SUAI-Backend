#pragma once
#include<iostream>
#include <string>
#include "Base_class.h"
using namespace std;

class Electricity : public Engine
{
public: 
	unsigned char t = 360; // ������������� ����������
	string c2 = "on";

public: 
	Electricity(float a, float q){A = a; Q = q;} // ����������� � �����������
	Electricity() {};
	~Electricity() { cout << "destroying variables" << endl; }

	void Power() // ������������� �������
	{
		cout << "power: " << A / t << endl;
	}
	void �haracteristic() override
	{
		cout << "condition: " << c2 << "\n" << endl;
	}
};
