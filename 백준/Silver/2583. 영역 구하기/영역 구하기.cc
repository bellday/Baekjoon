#include <iostream>
#include <vector>
#include <queue>
#include<algorithm>
using namespace std;
vector<int> Area;
struct Pos {
	int row;
	int col;
};

vector<vector<int>> Graph;
vector<vector<int>> Visit;
int M, N, K;

void input() {
	cin >> M >> N >> K;
	Graph = vector<vector<int>>(M, vector<int>(N));
	Visit = vector<vector<int>>(M, vector<int>(N));
	for (int i = 0; i < K; i++) {
		int startX, startY, EndX, EndY;

		cin >> startX >> startY >> EndX >> EndY;
		for (int j = startY ; j < EndY; j++) {
			for (int k = startX ; k < EndX; k++) {
				Graph[j][k] = 1; // 못가는 곳 설정
			}
		}
	}
}
void bfs(int row, int col) {
	queue<Pos> Q;
	Q.push({ row,col });
	Visit[row][col] = 1;
	int AreaSize = 0;
	int dr[4] = { -1,1,0,0 };
	int dc[4] = { 0,0,-1,1 };

	while (!Q.empty()) {
		Pos now = Q.front(); Q.pop();
		int R = now.row;
		int C = now.col;
		AreaSize++;
		for (int i = 0; i < 4; i++) {
			int NextR = R + dr[i];
			int NextC = C + dc[i];
			if (0 > NextR or NextR >= M or 0 > NextC or NextC >= N)
				continue;
			if (Graph[NextR][NextC] != 0)continue;
			if (Visit[NextR][NextC] == 1) continue;
			Visit[NextR][NextC] = 1;
			Q.push({ NextR,NextC });
		}
	}
	Area.push_back(AreaSize);
}

int main() {
	input();
	int count = 0;
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			if (Graph[i][j] == 0 and Visit[i][j] == 0) {
				count++; //갯수
				bfs(i, j);
			}
		}
	}
	cout << count << "\n";
	sort(Area.begin(), Area.end());
	for (int i = 0; i < Area.size(); i++)
		cout << Area[i] << " ";
}