#include <iostream>
#include <vector>
#include <queue>

using namespace std;
vector<vector<vector<int>>> Graph;
vector<vector<vector<int>>> Visit;
int M, N, H;
struct Pos {
	int Height;
	int Row;
	int Col;
};
queue<Pos> Q;
void input() {
	cin >> M >> N >> H;
	Graph = vector<vector<vector<int>>>(H, vector<vector<int>>(N, vector<int>(M)));

	Visit = vector<vector<vector<int>>>(H, vector<vector<int>>(N, vector<int>(M)));
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				cin >> Graph[i][j][k];
				if (Graph[i][j][k] == 1) {
					Q.push({ i,j,k });
					Visit[i][j][k] = 1;
				}
			}
		}
	}
}

void bfs() {
	int dh[6] = {1,-1,0,0,0,0};
	int dr[6] = {0,0,-1,1,0,0};
	int dc[6] = {0,0,0,0,-1,1};

	while (!Q.empty()) {
		Pos now = Q.front(); Q.pop();
		int Height = now.Height;
		int Row = now.Row;
		int Col = now.Col;

		for (int i = 0; i < 6; i++) {
			int NextHeight = Height + dh[i];
			int NextRow = Row + dr[i];
			int NextCol = Col + dc[i];

			if (0 > NextHeight or NextHeight >= H or 0 > NextRow or NextRow >= N or 0 > NextCol or NextCol >= M)
				continue;
			if (Visit[NextHeight][NextRow][NextCol] != 0)continue;
			if (Graph[NextHeight][NextRow][NextCol] == -1)continue; // 토마토 없을 경우
			Visit[NextHeight][NextRow][NextCol] = Visit[Height][Row][Col] + 1;
			Q.push({ NextHeight,NextRow,NextCol });
		}
	}
}

void calc() {
	int IsZero = 0;
	int ans = 0;
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				if (Visit[i][j][k] == 0 && Graph[i][j][k] == 0)// 안익은 토마토인데 방문하지 않았을 경우
				{
					IsZero = 1;
					break;
				}
				if (Visit[i][j][k] > ans)
					ans = Visit[i][j][k];
			}
		}
	}
	if (IsZero == 1)
		cout << -1;
	else
		cout << ans - 1;
}

int main() {
	input();
	bfs();
	calc();
}