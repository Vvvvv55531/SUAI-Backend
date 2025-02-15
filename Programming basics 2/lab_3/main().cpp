#include <iostream>
#include "Base_class.h"
#include "Level 1.1.h"
#include "Level 1.2.h"
#include "Level 1.3.h"
#include "Level 2.1.h"
#include "Level 2.2.h"
#include "Level 2.3.h"
using namespace std;

int main() // âûçîâ ıëåìåíòîâ êëàññà
{
	Engine n(1232, 2894); // áàçîâûé êëàññ
	n.Ñharacteristic();
	Engine m(2894);
	m.Ñharacteristic();
	Engine p;
	p.Ñharacteristic();
	p.Condition();

	Petrol v(2894); // êëàññû ïåğâîãî óğîâíÿ
	v.Efficiency();
	Petrol t;
	t.Ñharacteristic();
	Electricity a(1232, 2894);
	a.Power();
	Electricity i;
	i.Ñharacteristic();
	Kerosene g(1232, 2894);
	g.Fuel_consumption();
	Kerosene j;
	j.Ñharacteristic();

	Hybrid_car f; // êëàññû âòîğîãî óğîâíÿ
	f.Ñharacteristic();
	Rocket r;
	r.Ñharacteristic();
	Plane k;
	k.Ñharacteristic();
}
