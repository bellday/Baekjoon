#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;
struct position {
	int row;
	int col;
};
int N, M;
vector<vector<int>> graph;
vector<vector<int>> Minus;
vector<vector<int>> visit;
vector<vector<int>> visit2;
void input() {
	cin >> N >> M;
	graph = vector<vector<int>>(N, vector<int>(M));
	Minus = vector<vector<int>>(N, vector<int>(M));
	visit = vector<vector<int>>(N, vector<int>(M));
	visit2 = vector<vector<int>>(N, vector<int>(M));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> graph[i][j];
		}
	}
}

void bfs(int row, int col) {
	int dr[4] = { -1,1,0,0 };
	int dc[4] = { 0,0,-1,1 };
	queue<position> Q;
	Q.push({ row,col });
	visit[row][col] = 1;

	while (!Q.empty()) {
		position now = Q.front(); Q.pop();
		int NowRow = now.row;
		int NowCol = now.col;
		int MinusValue = 0;

		for (int i = 0; i < 4; i++) {
			int NextRow = NowRow + dr[i];
			int NextCol = NowCol + dc[i];

			if (0 > NextRow or NextRow >= N or 0 > NextCol or NextCol >= M)
				continue;
			if (graph[NextRow][NextCol] == 0) {
				MinusValue++;
				continue;
			}
			if (visit[NextRow][NextCol] != 0) continue;
			visit[NextRow][NextCol] = 1;
			Q.push({ NextRow,NextCol });

		}
		Minus[NowRow][NowCol] = MinusValue;
	}
}
void calc() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			graph[i][j] -= Minus[i][j];
			if (graph[i][j] < 0)graph[i][j] = 0;
			Minus[i][j] = 0; //초기화
			visit[i][j] = 0; //초기화
		}
	}
}
int IsTwo(int row,int col) {
	visit2[row][col] = 1;
	int dr[4] = { -1,1,0,0 };
	int dc[4] = { 0,0,-1,1 };
	queue<position> Q;
	Q.push({ row,col });
	while (!Q.empty()) {
		position now = Q.front(); Q.pop();
		int R = now.row;
		int C = now.col;

		for (int i = 0; i < 4; i++) {
			int NR = R + dr[i];
			int NC = C + dc[i];
			if (0 > NR or NR >= N or 0 > NC or NC >= M) continue;
			if (graph[NR][NC] == 0) continue;
			if (visit2[NR][NC] != 0)continue;
			visit2[NR][NC] = 1;
			Q.push({ NR,NC });
		}
	}
	return 1;
}
int main() {
	input();
	int flag = 0;
	int day = 0;
	while (1) {
		int Iszero = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (graph[i][j]>0 and visit[i][j]==0)
					bfs(i,j);
			}
		}
		calc();
		day++;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (graph[i][j] > 0 and visit2[i][j] == 0)
				{
					Iszero += IsTwo(i,j);
				}
			}
		}
		//visit2 초기화
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				visit2[i][j] = 0;
			}
		}


		if (Iszero == 0) {
			flag = 1;
			break;
		}
		else if (Iszero > 1) {
			break;
		}
	}
	if (flag == 1) {
		cout << 0;
	}
	else
		cout << day;
}

