#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, P;
	long long Score;
	cin >> N >> Score >> P;

	vector<long long> MAP;
	MAP = vector<long long>(N);

	

	for (int i = 0; i < N; i++) {
		cin >> MAP[i];
	}
	MAP.push_back(Score);
	sort(MAP.begin(), MAP.end());

	int ans = 0;
	int same = 0;
	for (int i = 0; i < MAP.size(); i++) {

		if (MAP[i] > Score) {
			ans++;
		}
		else if (MAP[i] == Score)
			same++;
	}
	if (ans  + same > P)
		cout << -1;
	else
		cout << ans + 1;
}