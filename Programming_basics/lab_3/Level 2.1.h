#pragma once
#include<iostream>
#include <string>
#include "Level 1.1.h"
#include "Level 1.2.h"
using namespace std;

class Hybrid_car : public Petrol, public Electricity // ������������ �������
{
private:
	string c3 = "wound up"; // ������������� ����������

public:
	Hybrid_car(){} // ����������� � �����������
	~Hybrid_car(){cout << "destroying variables" << endl;}

	void �haracteristic() override // ������������� �������
	{
		cout << "\nGeneral condition of transport:" 
		<< "\ninternal combustion engine: " 
		<< c1 << "\nelectric engine: " << c2 << "\ncar: " << c3 << endl;
	}
};
