#include <iostream>
#include <vector>
#include <queue>

using namespace std;
vector<vector<int>> Graph;
vector<vector<int>> Visit;
int KnightRow, KnightCol;
int EndRow, EndCol;
struct Pos
{
	int row; 
	int col;
};
void init() {
	Graph = vector<vector<int>>();
	Visit = vector<vector<int>>();
	KnightRow = 0; KnightCol = 0;
	EndRow = 0; EndCol = 0;
}
void input() {
	int Size;
	cin >> Size;
	Graph = vector<vector<int>>(Size, vector<int>(Size));
	Visit = vector<vector<int>>(Size, vector<int>(Size));
	cin >> KnightRow >> KnightCol;
	cin >> EndRow >> EndCol;
}

void calc() {
	queue<Pos> Q;
	Q.push({ KnightRow,KnightCol });
	Visit[KnightRow][KnightCol] = 1;

	int dr[8] = { -2,-1,1,2,2,1,-1,-2 };
	int dc[8] = {  1,2,2,1,-1,-2,-2,-1};

	

	while (!Q.empty()) {
		Pos now = Q.front(); Q.pop();
		int R = now.row;
		int C = now.col;

		if (R == EndRow and C == EndCol) {
			cout  << Visit[R][C] - 1 << "\n";
			break;
		}

		for (int i = 0; i < 8; i++) {
			int NextR = R + dr[i];
			int NextC = C + dc[i];

			if (0 > NextR or NextR >= Graph.size() or 0 > NextC or NextC >= Graph.size())
				continue;
			if (Visit[NextR][NextC] != 0)continue;
			Visit[NextR][NextC] = Visit[R][C] + 1;
			Q.push({ NextR,NextC });
		}

	}
}

int main() {
	int TC;
	cin >> TC;
	for (int i = 0; i < TC; i++) {
		init();
		input();
		calc();
	}
}