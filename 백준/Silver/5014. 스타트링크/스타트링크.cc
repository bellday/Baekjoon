#include <iostream>
#include <queue>
#include <vector>

using namespace std;
vector<int> MAP;
int F, S, G, U, D;
void input() {
	cin >> F >> S >> G >> U >> D; // F층으로 이루어짐. 강호가 있는 층. 목표층.. 위로가는 층 , 아래로 가는 층
	MAP = vector<int>(F+1);
}
void bfs(int now) {
	queue<int> Q;
	Q.push(now);
	MAP[now] = 1;
	while (!Q.empty()) {
		int Curstory = Q.front(); Q.pop();
		int Upstory = Curstory + U;
		int Downstory = Curstory - D;
		if (Upstory <= F and MAP[Upstory] == 0) {
			MAP[Upstory] = MAP[Curstory] + 1;
			Q.push(Upstory);
		}
		if (Downstory>0 and MAP[Downstory] == 0) {
			MAP[Downstory] = MAP[Curstory] + 1;
			Q.push(Downstory);
		}
	}
	if (MAP[G] == 0)
		cout << "use the stairs";
	else
		cout << MAP[G] -1;
}

int main() {
	input();
	bfs(S);
}