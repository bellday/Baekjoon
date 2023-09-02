#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int Input;
int DAT[1000001] = { 0, };
int ans = 2134567890;

struct Info {
	int Number;
	int Times;
};
void calc(int Num) {
	queue<Info> Q;
	Q.push({ Num,0 });

	while (!Q.empty()) {
		Info now = Q.front(); Q.pop();
		int N = now.Number;
		int T = now.Times;
		if (N == 1 and ans > T) {
			ans = T;
		}

		if (N % 3 == 0 and DAT[N / 3] == 0) {
			DAT[N / 3] = 1;
			Q.push({ N / 3,T + 1 });
		}

		if (N % 2 == 0 and DAT[N / 2] == 0) {
			DAT[N / 2] = 1;
			Q.push({ N / 2,T + 1 });
		}
		if (DAT[N - 1] == 0) {
			DAT[N - 1] = 1;
			Q.push({ N - 1,T + 1 });
		}
	}
}

int main() {
	cin >> Input;
	DAT[Input] = 1;
	calc(Input);
	cout << ans;
}