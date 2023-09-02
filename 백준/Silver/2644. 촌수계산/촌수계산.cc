#include <iostream>
#include <vector>

using namespace std;
int N;
vector<vector<int>> graph;
vector<int> visit;
int Start, End;
int rst = -1;
void input() {
	cin >> N;
	graph = vector<vector<int>>(N+1);
	visit = vector<int>(N + 1);
	cin >> Start >> End;
	int Size;
	cin >> Size;
	for (int i = 0; i < Size; i++) {
		int s, e;
		cin >> s >> e;
		graph[s].push_back(e);
		graph[e].push_back(s);
	}

}

void dfs(int S, int level) {
	visit[S] = 1;
	if (S == End) {
		rst = level;
	}
	for (int i = 0; i < graph[S].size(); i++) {
		if (visit[graph[S][i]] == 0) {
			dfs(graph[S][i], level + 1);
		}
	}
}
int main() {
	input();
	dfs(Start, 0);
	cout << rst;
}
