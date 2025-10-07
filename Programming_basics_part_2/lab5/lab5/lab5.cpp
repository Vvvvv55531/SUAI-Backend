#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<random>
using namespace std;


void mas(vector<double>& m)
{
    int x = m.size();
    for (int i = 1; i < x - 1; i++)
    {
        if ((m[i - 1] > m[i]) && (m[i] < m[i + 1]))
        {
            m[i] = 0;
        }
    }
}


void slova2(vector <string>& a, string sl)
{
    string s2 = "";
    for (string s : a)
    {
        if (sl.size() == s.size())
        {
            s2 += s;
        }
    }
    a.push_back(s2);
}


void slova(string& s, string sl)
{
    stringstream ss(s);
    string word;
    vector <string> a;
    while (!ss.eof())
    {
        ss >> word;
        a.push_back(word);
    }
    slova2(a, sl);
    s = "";
    for (string s1 : a)
    {
        s += s1 + ' ';
    }

}
int main()
{
    int d, p;
    cin >> d;
    if (d <= 2)
    {
        return 0;
    }
    vector <double> a(d);
    for (int i = 0; i < d; i++)
    {
        cin >> p;
        if (p < 10 || p > 150)
        {
            return 0;
        }
        a[i] = p;
    }
    cout << "a[ ";
    for (int i = 0; i < d; i++) cout << a[i] << " ";
    cout << "] " << endl;

    int d2;
    cin >> d2;
    if (d2 <= 2)
    {
        return 0;
    }
    double random;
    vector <double> b(d2);
    srand(time(0));
    for (int n = 0; n < d2; n++)
    {
        random = (rand() % 14001 + 1000) / 100.0;
        b[n] = random;
    }
    cout << "b[ ";
    for (int n = 0; n < d2; n++) cout << b[n] << " ";
    cout << "] " << endl;

    mas(a);
    cout << "a[ ";
    for (int i = 0; i < d; i++) cout << a[i] << " ";
    cout << "] " << endl;

    mas(b);
    cout << "b[ ";
    for (int n = 0; n < d2; n++) cout << b[n] << " ";
    cout << "] " << endl;

    string s, sl, mud;
    getline(cin, mud);
    getline(cin, s);
    cin >> sl;
    slova(s, sl);
    cout << s;
    return 0;
}

