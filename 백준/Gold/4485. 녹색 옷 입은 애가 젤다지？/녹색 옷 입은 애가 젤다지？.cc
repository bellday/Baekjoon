#include <iostream>
#include <vector>
#include<queue>

using namespace std;

struct position {
	int value;
	int row;
	int col;
	bool operator<(position p) const{
		if (p.value >= value) return false;
		if (p.value < value) return true;
		return false;
	}
};

vector<vector<int>> graph;
vector<vector<int>> visit;
void input(int s) {
	graph = vector<vector<int>>(s, vector<int>(s));
	visit = vector<vector<int>>(s, vector<int>(s));
	for (int i = 0; i < s; i++) {
		for (int j = 0; j < s; j++) {
			cin >> graph[i][j];
		}
	}
}

void dijkstra(int times) {
	priority_queue<position> pq;

	int dr[4] = { -1,1,0,0 };
	int dc[4] = { 0,0,-1,1 };

	visit[0][0] = 1;
	pq.push({ graph[0][0],0,0 });
	int rst = 0;
	while (!pq.empty()) {
		position now = pq.top(); pq.pop();
		int value = now.value;
		int row = now.row;
		int col = now.col;

		if (row == graph.size() - 1 and col == graph.size() - 1)
		{
			rst = value;
			break;
		}

		for (int i = 0; i < 4; i++) {
			int next_row = row + dr[i];
			int next_col = col + dc[i];

			if (0 > next_row or next_row >= graph.size() or 0 > next_col or next_col >= graph.size())
				continue;
			if (visit[next_row][next_col] == 1) continue;
			visit[next_row][next_col] = 1;
			int next_val = value + graph[next_row][next_col];
			pq.push({ next_val,next_row,next_col });

		}
	}
	cout << "Problem " << times<< ": " << rst << endl;

}


int main() {
	int i = 1;
	while (1)
	{
		int size;
		cin >> size;
		if (size != 0)
		{
			input(size);
			dijkstra(i);
			i++;
		}
		else if (size == 0)
		{
			break;
		}
	}
}