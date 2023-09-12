#include <iostream>
#include <vector>
#include <string>

using namespace std;
int N, M; // 갯수 M 칭호
struct Data {
	string S1;
	int Range;
};
vector<Data> MAP;

void input() {
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		string inputStr;
		int inputInt;
		cin >> inputStr >> inputInt;
		MAP.push_back({ inputStr,inputInt });
	}
}


int main() {
	ios::sync_with_stdio();
	cin.tie(NULL);
	cout.tie(NULL);
	input();
	for (int i = 0; i < M; i++) {
		int num;

		cin >> num;

		int left = 0;
		int right = N - 1;
		int mid = 0;
		while (left <= right) {
			mid = (left + right) / 2;
			if (MAP[mid].Range >= num) {
				right = mid - 1;
			}
			else {
				left = mid + 1;
			}
		}
		if (num > MAP[mid].Range)
			mid += 1;

		cout << MAP[mid].S1 << "\n";
	}
}