#include <iostream>
#include <vector>
#include <algorithm>
#include<math.h>
using namespace std;
typedef vector<int> VI;

void solve(vector<int> v, int n, int c, int d)
{

	auto iter = min_element(v.begin(), v.end());

	int initial = *iter;

	int sumcol = 0;
	for (int i = 0; i < n; i++)
	{

		auto it = find(v.begin(), v.end(), initial);
		if (it == v.end())
		{
	
			cout<<"NO"<<"\n";
			return;
		}
		else
		{
			int indice = distance(v.begin(), it);
			v.erase(v.begin() + indice);
	
		}
		for (int j = 1; j < n; j++)
		{
			if (j == 1)
				sumcol = initial + c;
			else
				sumcol = sumcol + c;

			auto it2 = find(v.begin(), v.end(), sumcol);
			if (it2 == v.end())
			{
					cout<<"NO"<<"\n";
					return;
			}
			else
			{
				int indice2 = distance(v.begin(), it2);
				v.erase(v.begin() + indice2);
			}
		}
		initial = initial + d;
	}
	cout<<"YES"<<"\n";
	return;
}
int main()
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
	
		solve(v, n, c, d);
	}
}