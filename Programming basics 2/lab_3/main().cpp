#include <iostream>
#include "Base_class.h"
#include "Level 1.1.h"
#include "Level 1.2.h"
#include "Level 1.3.h"
#include "Level 2.1.h"
#include "Level 2.2.h"
#include "Level 2.3.h"
using namespace std;

int main() // ����� ��������� ������
{
	Engine n(1232, 2894); // ������� �����
	n.�haracteristic();
	Engine m(2894);
	m.�haracteristic();
	Engine p;
	p.�haracteristic();
	p.Condition();

	Petrol v(2894); // ������ ������� ������
	v.Efficiency();
	Petrol t;
	t.�haracteristic();
	Electricity a(1232, 2894);
	a.Power();
	Electricity i;
	i.�haracteristic();
	Kerosene g(1232, 2894);
	g.Fuel_consumption();
	Kerosene j;
	j.�haracteristic();

	Hybrid_car f; // ������ ������� ������
	f.�haracteristic();
	Rocket r;
	r.�haracteristic();
	Plane k;
	k.�haracteristic();
}
