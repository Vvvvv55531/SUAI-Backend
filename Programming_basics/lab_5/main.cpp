#include <iostream> // ������������ ����� � ��� ���������
#include <vector>
#include <algorithm>
#include <functional>
#include <iterator>
#include <ctime>
#include <chrono>
#include <execution>
#include <thread>

using namespace std;


template <typename T> // ������ ������� ����������
T Completion(T& v)
{
	int cmax;
	cout << "������� ����� ��������� L:" << endl;
	cin >> cmax;
	for (int c = 0; c < cmax; c++) { v.insert(v.end(), rand() % 10); }
	return v;
}


void Timer(chrono::steady_clock::time_point st) // ����� �������
{
	auto end = chrono::high_resolution_clock::now();
	chrono::duration<float> duration = end - st;
	cout << "\n" << duration.count() << "\n" << endl;
}


int main()
{
	setlocale(LC_ALL, "ru"); // ru; rand()
	srand(time(NULL));

	vector<int> L; // ������������� ��������� L
	Completion(L);
	vector<int> L1 = L;
	
	int E1, E2;
	cout << "\n������� E1:" << endl; // ���� �������� ��������� E1, E2
	cin >> E1;
	cout << "\n������� E2:" << endl;
	cin >> E2;
	cout << endl;

	function<int(int)> f; // ��������, ������� � ���� ������-���������
	function<bool(int)> f1;
	f = [&E2, &f1](int a)
	{
		if (f1(a) == true) { return E2; }
		else { return a; }
	};
	f1 = [&E1](int a) {return a == E1; };

	cout << "\n���������:\n" << endl; // ����� ������ ���������� ����
	int num_threads = thread::hardware_concurrency();

	cout << "��� �������� ����������"; // ��������� ���������� ��� ��������� �������� ����������
	auto start = chrono::high_resolution_clock::now(); // ����� ���������
	transform(L.begin(), L.end(), L.begin(), f); 
	Timer(start);

	cout << "� ��������� sequenced_policy"; // ��������� ���������� � ��������� sequenced_policy (seq)
	L = L1;
	start = chrono::high_resolution_clock::now();
	transform(execution::seq, L.begin(), L.end(), L.begin(), f); 
	Timer(start);
	
	cout << "� ��������� parallel_policy"; // ��������� ���������� � ��������� parallel_policy (par)
	L = L1;
	start = chrono::high_resolution_clock::now();
	transform(execution::par, L.begin(), L.end(), L.begin(), f);
	Timer(start);

	cout << "� ��������� parallel_unsequenced_policy"; // ��������� ���������� � ��������� parallel_unsequenced_policy (par_unseq)
	L = L1;
	start = chrono::high_resolution_clock::now();
	transform(execution::par_unseq, L.begin(), L.end(), L.begin(), f);
	Timer(start);

	cout << "���������� ������������� ������� - " << num_threads << endl; // ������� ������� ����� ��������� � ���� �����

	return 0;
}
