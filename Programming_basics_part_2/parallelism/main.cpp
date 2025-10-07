#include <iostream> // библиотечные файлы и все остальное
#include <vector>
#include <algorithm>
#include <functional>
#include <iterator>
#include <ctime>
#include <chrono>
#include <execution>
#include <thread>

using namespace std;


template <typename T> // шаблон функции заполнения
T Completion(T& v)
{
	int cmax;
	cout << "Введите длину коллекции L:" << endl;
	cin >> cmax;
	for (int c = 0; c < cmax; c++) { v.insert(v.end(), rand() % 10); }
	return v;
}


void Timer(chrono::steady_clock::time_point st) // замер времени
{
	auto end = chrono::high_resolution_clock::now();
	chrono::duration<float> duration = end - st;
	cout << "\n" << duration.count() << "\n" << endl;
}


int main()
{
	setlocale(LC_ALL, "ru"); // ru; rand()
	srand(time(NULL));

	vector<int> L; // инициализация коллекции L
	Completion(L);
	vector<int> L1 = L;
	
	int E1, E2;
	cout << "\nВведите E1:" << endl; // ввод значений элементов E1, E2
	cin >> E1;
	cout << "\nВведите E2:" << endl;
	cin >> E2;
	cout << endl;

	function<int(int)> f; // предикат, функция в виде лямбда-выражения
	function<bool(int)> f1;
	f = [&E2, &f1](int a)
	{
		if (f1(a) == true) { return E2; }
		else { return a; }
	};
	f1 = [&E1](int a) {return a == E1; };

	cout << "\nРезультат:\n" << endl; // вывод итогов выполнения кода
	int num_threads = thread::hardware_concurrency();

	cout << "Без политики выполнения"; // обработка контейнера без указанной политики выполнения
	auto start = chrono::high_resolution_clock::now(); // время обработки
	transform(L.begin(), L.end(), L.begin(), f); 
	Timer(start);

	cout << "С политикой sequenced_policy"; // обработка контейнера с политикой sequenced_policy (seq)
	L = L1;
	start = chrono::high_resolution_clock::now();
	transform(execution::seq, L.begin(), L.end(), L.begin(), f); 
	Timer(start);
	
	cout << "С политикой parallel_policy"; // обработка контейнера с политикой parallel_policy (par)
	L = L1;
	start = chrono::high_resolution_clock::now();
	transform(execution::par, L.begin(), L.end(), L.begin(), f);
	Timer(start);

	cout << "С политикой parallel_unsequenced_policy"; // обработка контейнера с политикой parallel_unsequenced_policy (par_unseq)
	L = L1;
	start = chrono::high_resolution_clock::now();
	transform(execution::par_unseq, L.begin(), L.end(), L.begin(), f);
	Timer(start);

	cout << "Количество одновременных потоков - " << num_threads << endl; // сколько потоков можно запустить в одно время

	return 0;
}
