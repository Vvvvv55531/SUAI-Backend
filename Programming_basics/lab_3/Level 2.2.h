#pragma once
#include<iostream>
#include <string>
#include "Level 1.1.h"
#include "Level 1.2.h"
#include "Level 1.3.h"
using namespace std;

class Rocket : public Petrol, public Electricity, public Kerosene // ������������ �������
{
private:
	string c3 = "at rest"; // ������������� ����������

public:
	Rocket(){} // ����������� � �����������
	~Rocket(){cout << "destroying variables" << endl;}

	void �haracteristic() override // ������������� �������
	{
		cout << "\nGeneral condition of transport:"
			<< "\ninternal combustion engine: "
			<< c1 << "\nelectric engine: " << c2 << "\nrocket engine: " << c4 << "\nrocket: " << c3 << endl;
	}
};
