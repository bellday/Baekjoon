#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

struct Time
{
	int start;
	int end;
};
vector<Time> list;
vector<Time> table;
int N1, N2;

void input()
{
	int maximum = 0;
	int size;
	cin >> size;
	for (int i = 0; i < size; i++)
	{
		Time in;
		cin >> in.start >> in.end;
		list.push_back({ in.start, in.end });
		if (in.end > maximum)
		{
			maximum = in.end;
		}
	}

}

bool comp(Time one, Time second)
{


	if (one.end < second.end) return true;
	if (one.end > second.end) return false;
	if (one.end == second.end)
		if (one.start < second.start) return true;
		else return false;
	return false;
}



void greedy()
{
	sort(list.begin(), list.end(), comp);
	int cnt = 1; //첫번째 회의는 가능
	table.push_back({ list[0].start, list[0].end });
	for (int i = 1; i < list.size(); i++)
	{
		int start_time = list[i].start;
		if (start_time >= table[0].end) //갱신 가능 여부 확인
		{
			cnt++;
			table[0].start = start_time;
			table[0].end = list[i].end;
		}
	}
	cout << cnt;
}

int main()
{
	input();
	greedy();
}
