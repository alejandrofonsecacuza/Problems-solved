#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef vector<int> VI;

void solve(vector<int> v, int n, int c, int d)
{
/*	for (int i : v)
	{
		cout << i << ", ";
	}
	cout << endl;*/
	auto iter = min_element(v.begin(), v.end());

	int initial = *iter;
//	cout << "min " << *iter << endl;
	int sumcol = 0;
	for (int i = 0; i < n; i++)
	{
//		cout << "Buscando: " << initial << endl;
		//cout << *find(v.begin(), v.end(), initial) << endl;
		auto it = find(v.begin(), v.end(), initial);
		if (it == v.end())
		{
	//		cout << "No se encontro" << endl;
			cout<<"NO"<<"\n";
			return;
		}
		else
		{
			int indice = distance(v.begin(), it);
			v.erase(v.begin() + indice);
	/*		cout << "Se encontro y se borro" << endl;
			
			for (int i : v)
			{
				cout << i << ", ";
			}
			cout<<endl;*/
		}
		for (int j = 1; j < n; j++)
		{
			if (j == 1)
				sumcol = initial + c;
			else
				sumcol = sumcol + c;
	//		cout << "Buscando: " << sumcol << endl;
			auto it2 = find(v.begin(), v.end(), sumcol);
			if (it2 == v.end())
			{
//				cout << "No se encontro" << endl;
					cout<<"NO"<<"\n";
					return;
			}
			else
			{
				int indice2 = distance(v.begin(), it2);
				v.erase(v.begin() + indice2);
	/*			cout << "Se encontro y se borro" << endl;
				for (int i : v)
				{
					cout << i << ", ";
				}
				cout<<endl;*/
			}
		}
		initial = initial + d;
	}
	cout<<"YES"<<"\n";
	return;
}
int main(int argc, char *argv[])
{
	int t, n, c, d;

	cin >> t;

	while (t--)
	{
		vector<int> v;
		cin >> n >> c >> d;
		int y = pow(n, 2);
		int ni;
		while (y--)
		{
			cin >> ni;
			v.push_back(ni);
		}
	//	cout << "solve(v," << n << "," << c << "," << d << ")" << endl;
		solve(v, n, c, d);
	}
}