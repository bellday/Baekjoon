#include <iostream>
#include <vector>
#include <queue>
using namespace std;
vector<int> Visit;
vector<vector<int>> MAP;
int Minimmum = 2134567890;
int rst = 0;
int ans = 0;
int  N, M;
void input() {
	cin >> N >> M; // 유저의 수, 친구 관계의 수
	Visit = vector<int>(N + 1);
	MAP = vector<vector<int>>(N + 1);
	for (int i = 0; i < M; i++) {
		int A, B;
		cin >> A >> B;
		MAP[A].push_back(B);
		MAP[B].push_back(A);
	}
}

void init(int Value) {
	rst = 0;
	for (int i = 0; i < N + 1; i++){
		rst += Visit[i];
		Visit[i] = 0;
	}
	if (Minimmum > rst)
	{
		Minimmum = rst;
		ans = Value;
	}
	rst = 0;
}

void bfs(int Val) {
	queue<int> Q;
	Q.push(Val);
	Visit[Val] = 1;

	while (!Q.empty())
	{
		int now = Q.front(); Q.pop();

		for (int i = 0; i < MAP[now].size(); i++) {
			if (Visit[MAP[now][i]] == 0) {
				Visit[MAP[now][i]] = Visit[now] + 1;
				Q.push(MAP[now][i]);
			}
		}

	}

}

int main() {
	input();
	for (int i = 1; i < N; i++) {
		bfs(i);
		init(i);
	}
	cout << ans;
}