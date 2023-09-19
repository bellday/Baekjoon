#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;
vector<vector<char>> MAP;
vector<vector<int>> Visit1;
vector<vector<int>> Visit2;

struct Pos
{
	int row; 
	int col;
	char alpha;
};
int Size;
void input() {
	
	cin >> Size;
	MAP = vector<vector<char>>(Size,vector<char> (Size));
	Visit1 = vector<vector<int>>(Size, vector<int>(Size));
	Visit2 = vector<vector<int>>(Size, vector<int>(Size));
	for (int i = 0; i < Size; i++) {
		for (int j = 0; j < Size; j++) {
			cin >> MAP[i][j];
		}
	}
}

void bfs(int row, int col, int IsNormal) {
	// 1이면 정상 0이면 비정상
	queue<Pos> Q;
	Q.push({ row,col,MAP[row][col] });
	if (IsNormal == 1) Visit1[row][col] = 1;
	else if (IsNormal==0)Visit2[row][col] = 1;

	int dr[4] = { -1,1,0,0 };
	int dc[4] = { 0,0,-1,1 };

	while (!Q.empty()) {
		Pos now = Q.front(); Q.pop();
		int R = now.row;
		int C = now.col;
		char Data = now.alpha;

		for (int i = 0; i < 4; i++) {
			int NextR = R + dr[i];
			int NextC = C + dc[i];
			if (0 > NextR or NextR >= Size or 0 > NextC or NextC >= Size)
				continue;
			if (IsNormal == 1 and MAP[NextR][NextC] != Data) continue;
			if (IsNormal == 0 and Data == 'G' and MAP[NextR][NextC] == 'B')continue;
			else if (IsNormal == 0 and Data == 'R' and MAP[NextR][NextC] == 'B')continue;
			else if (IsNormal == 0 and Data == 'B' and MAP[NextR][NextC] != Data)continue;
			if (IsNormal == 1 and Visit1[NextR][NextC] != 0)continue;
			else if (IsNormal == 0 and Visit2[NextR][NextC] != 0)continue;

			if (IsNormal==1) Visit1[NextR][NextC] = 1;
			else if (IsNormal == 0) Visit2[NextR][NextC] = 1;
			Q.push({ NextR, NextC,MAP[NextR][NextC] });
		}
	}
}

int main() {
	input();

	int ans1 = 0;
	int ans2 = 0;
	for (int i = 0; i < Size; i++) {
		for (int j = 0; j < Size; j++) {
			if (Visit1[i][j] == 0) {
				bfs(i, j,1);
				ans1++;
			}
		}
	}
	
	for (int i = 0; i < Size; i++) {
		for (int j = 0; j < Size; j++) {
			if (Visit2[i][j] == 0) {
				bfs(i, j,0);
				ans2++;
			}
		}
	}
	cout << ans1 << " " << ans2;
}