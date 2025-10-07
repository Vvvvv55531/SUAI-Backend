#pragma once
#include<iostream>
#include <string>
using namespace std;

class Engine
{	
public: 
	float A = 0, Q = 0; // инициализация переменных
	string c = "on";

public: 
	Engine(float a, float b){A = a; Q = b;} // кострукторы и деструкторы
	Engine(float b){Q = b;}
	Engine(){}
	~Engine(){cout << "destroying variables" << endl;}

	virtual void Characteristic() // инициализация методов
	{
		cout << "A:" << A << "," 
		"Q:" << Q << endl; 
	}
	void Condition()
	{
		cout << "condition: " << c << "\n" << endl; 
	}
};
