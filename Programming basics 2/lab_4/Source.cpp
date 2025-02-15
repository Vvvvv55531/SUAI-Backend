#include <iostream> // ������������ ����� � ��� ���������
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <ctime>
#include <chrono>

using namespace std; 

template <typename T> // ������ ������� ����������
T Completion(T &v)
{
	int cmax;
	cout << "������� ����� ��������� L:" << endl;
	cin >> cmax;
	for (int c = 0; c < cmax; c++) {v.insert(v.end(), rand() % 10);}
	return v;
}

template <typename T1, typename T2> // ���������� ��� map
map<T1, T2> Completion(map<T1, T2> &v)
{
	int cmax;
	cout << "������� ����� ��������� L map:" << endl;
	cin >> cmax;
	for (int c = 0; c < cmax; c++) {v.insert(v.end(), make_pair(c, rand() % 10));}
	return v;
}

template <typename T> // ������ ������� ������
void Print(T v)
{
	cout << "L = [ ";
	for (auto i : v) cout << i << " ";
	cout << "]\n" << endl;
}

template <typename T1, typename T2> // ���������� ��� map
void Print(map<T1, T2> v)
{
	cout << "Lm = [ ";
	for (auto i : v) cout << "(" << i.first << "," << i.second << ") ";
	cout << "]\n" << endl;
}

void Timer(chrono::steady_clock::time_point st) // ����� �������
{
	auto end = chrono::high_resolution_clock::now();
	chrono::duration<float> duration = end - st;
	cout << "����� ���������:\n";
	cout << duration.count() << endl << endl;
}

template <typename T> // ��������� multiset
void Transform(T &v, int e, function<bool(int)> f)
{
	multiset<int> v0;
	for (auto i : v)
	{ 
		if (f(i) == true) {v0.insert(v0.end(), e);}
		else {v0.insert(v0.end(), i);}
	}
	v = v0;
}

template <typename T1, typename T2> // ���������� ��� map
void Transform(map<T1, T2> &v, int e, function<bool(int)> f)
{
	map<int, int> v0;
	for (auto i : v)
	{
		if (f(i.first) == f(i.second))
		{
			if (f(i.first) == true)
			{v0.insert(v0.end(), make_pair(e, e));}
			if (f(i.first) == false)
			{v0.insert(v0.end(), make_pair(i.first, i.second));}
		}
		else {
			if (f(i.first) == true)
			{v0.insert(v0.end(), make_pair(e, i.second));}
			else
			{v0.insert(v0.end(), make_pair(i.first, e));}}
	}
	v = v0;
}

int main()
{
	setlocale(LC_ALL, "ru"); // ru; rand()
	srand(time(NULL));

	vector<int> L; // ������������� ��������� L � �������� �������
	Print(Completion(L));
	list<int> L1;
	Print(Completion(L1));
	multiset<int> L2;
	Print(Completion(L2));
	map<int, int> L3;
	Print(Completion(L3));

	int E1, E2;
	cout << "������� E1:" << endl; // ���� �������� ��������� E1, E2
	cin >> E1;
	cout << "\n������� E2:" << endl;
	cin >> E2;
	cout << endl;

	function<int(int)> f; // ��������, ������� � ���� ������-���������
	function<bool(int)> f1;
	f = [&E2, &f1](int a)
	{
		if (f1(a) == true) {return E2;}
		else {return a;}
	};
	f1 = [&E1](int a) {return a == E1;};

	auto start = chrono::high_resolution_clock::now(); // ����� ���������
	transform(L.begin(), L.end(), L.begin(), f); // ��������� �����������
	Print(L);
	Timer(start);

	start = chrono::high_resolution_clock::now();
	transform(L1.begin(), L1.end(), L1.begin(), f);
	Print(L1);
	Timer(start);
	
	start = chrono::high_resolution_clock::now();
	Transform(L2, E2, f1);
	Print(L2);
	Timer(start);

	start = chrono::high_resolution_clock::now();
	Transform(L3, E2, f1);
	Print(L3);
	Timer(start);

	return 0;
}
