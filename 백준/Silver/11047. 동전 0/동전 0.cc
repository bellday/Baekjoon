#include <iostream>
#include <vector>

using namespace std;
vector<int> MAP;
int n, k;
void input() {
	cin >> n >> k;
	MAP = vector<int>(n);
	for (int i = 0; i < n; i++)
	{
		cin >> MAP[i];
	}
		
}
int main() {
	input();
	int coins = 0;
	int value = n - 1;
	while (k != 0) {
		int nowCoin = MAP[value];
		int addValue = k / nowCoin;
		coins += k / nowCoin;
		k -= nowCoin * addValue;
		
		value -= 1;
	}
	cout << coins;
}