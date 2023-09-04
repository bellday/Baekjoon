#include <iostream>
#include <vector>

using namespace std;
int N, M;
vector<vector<int>> graph;
vector<int> visit;
void input() {
	cin >> N >> M;
	graph = vector<vector<int>>(N+1);
	visit = vector<int>(N + 1);
	for (int i = 0; i < M; i++) {
		int start, end;
		cin >> start >> end;
		graph[start].push_back(end);
		graph[end].push_back(start);
	}
}

void calc(int start) {

	for (int i = 0; i < graph[start].size(); i++) {
		if (visit[graph[start][i]] == 0) {
			visit[graph[start][i]] = 1;
			calc(graph[start][i]);
		}
	}

}

int main() {
	input();
	int cnt = 0;
	for (int i = 1; i < N + 1; i++) {
		if (visit[i] == 0) {
			cnt ++;
			calc(i);
		}
	}
	cout << cnt;

	
}