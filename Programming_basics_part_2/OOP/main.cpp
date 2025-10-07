#include <iostream>
#include "Base_class.h"
#include "Level_1.1.h"
#include "Level_1.2.h"
#include "Level_1.3.h"
#include "Level_2.1.h"
#include "Level_2.2.h"
#include "Level_2.3.h"
using namespace std;

int main() // вызов элементов класса
{
	Engine n(1232, 2894); // базовый класс
	n.Characteristic();
	Engine m(2894);
	m.Characteristic();
	Engine p;
	p.Characteristic();
	p.Condition();

	Petrol v(2894); // классы первого уровня
	v.Efficiency();
	Petrol t;
	t.Characteristic();
	Electricity a(1232, 2894);
	a.Power();
	Electricity i;
	i.Characteristic();
	Kerosene g(1232, 2894);
	g.Fuel_consumption();
	Kerosene j;
	j.Characteristic();

	Hybrid_car f; // классы второго уровня
	f.Characteristic();
	Rocket r;
	r.Characteristic();
	Plane k;
	k.Characteristic();
}
