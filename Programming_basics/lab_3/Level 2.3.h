#pragma once
#include<iostream>
#include <string>
#include "Level 1.2.h"
#include "Level 1.3.h"
using namespace std;

class Plane : public Electricity, public Kerosene // ������������ �������
{
private:
	string c3 = "on the ground"; // ������������� ����������

public:
	Plane(){} // ����������� � �����������
	~Plane(){cout << "destroying variables" << endl;}

	void �haracteristic() override // ������������� �������
	{
		cout << "\nGeneral condition of transport:"
			<< "\nelectric engine: " << c2 
			<< "\nrocket engine: " << c4 << "\nplane: " << c3 << "\n" << endl;
	}
};
