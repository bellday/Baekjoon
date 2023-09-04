#include <iostream>
#include <string>
#include <queue>
using namespace std;
vector<vector<int>> graph;
int startR = 0;  int startC=0;

struct Pos {
	int row;
	int col;
};
int N, M;
void input() {
	
	cin >> N >> M;
	graph = vector<vector<int>>(N,vector<int>(M));
	for (int i = 0; i < N; i++) {
		string inputstr;
		cin >> inputstr;

		for (int j = 0; j < inputstr.size(); j++) {

			if (inputstr[j] == 'I') {
				startR = i;
				startC = j;
				graph[i][j] = 2;
			}
			else if (inputstr[j] == 'O') {
				graph[i][j] = 0;
			}
			else if (inputstr[j] == 'P') {
				graph[i][j] = 1;
			}
			else if (inputstr[j] == 'X') {
				graph[i][j] = -1;
			}
		}
	}
}

int bfs() {
	queue<Pos>Q;
	vector<vector<int>> visit;
	visit = vector<vector<int>>(N, vector<int>(M));
	visit[startR][startC] = 1;
	int dr[4] = { -1,1,0,0 };
	int dc[4] = { 0,0,-1,1 };
	Q.push({ startR,startC });
	int cnt = 0;
	while (!Q.empty())
	{
		Pos now = Q.front(); Q.pop();
		int nR = now.row;
		int nC = now.col;

		for (int i = 0; i < 4; i++)
		{
			int nextrow = nR + dr[i];
			int nextcol = nC + dc[i];
			if (0 > nextrow or nextrow >= N or 0 > nextcol or nextcol >= M)
				continue;
			if (visit[nextrow][nextcol] != 0) continue;
			
			if(graph[nextrow][nextcol] == -1)continue;
			visit[nextrow][nextcol] = 1;
			Q.push({ nextrow,nextcol });
			if (graph[nextrow][nextcol] == 1) {
				cnt++;
			}
		}
	}
	return cnt;
}

int main() {
	input();
	int rst=bfs();
	if (rst == 0)
		cout << "TT";
	else
	{
		cout << rst;
	}
	
}