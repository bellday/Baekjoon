#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector <int> loca;
vector <int> DAT;
vector <int> vect;
int cnt = 0;
bool check(int lv, int end) {

	for (int i = 0; i < lv; i++)
	{
		if ((loca[i] == loca[lv]) or (abs(loca[lv] - loca[i]) == lv - i))
			return false;

	}
	return true;
}


void backtrack(int level, int end_point)
{
	// 종료 조건

	if (level == end_point)
	{
		cnt++;
		return;
	}

	for (int i = 0; i < end_point; i++)
	{
		
		loca[level] = i;
		if (check(level, end_point))
		{
			
			backtrack(level + 1, end_point);
		}
	}
}


int main()
{
	int size_of_chess;
	cin >> size_of_chess;
	vect.resize(size_of_chess);
	DAT.resize(size_of_chess);
	loca.resize(size_of_chess);
	backtrack(0, size_of_chess);
	cout << cnt;
}