#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
using namespace std;

struct BC {
	int row, col;
	int range, P;
};

int M, A;
vector<int> pos[2];
vector<BC> bc;
vector<vector<vector<int>>> graph; // [who 2개] [time M+1개] -> 충전 가능한 bc들(index)
void init() {
	M = A = 0;
	bc.clear();
}

void input() {
	cin >> M >> A;
	graph = vector<vector<vector<int>>>(2, vector<vector<int>>(M + 1));
	pos[0] = vector<int>(M + 1); // M개 크기로 생성
	pos[1] = vector<int>(M + 1); // M개 크기로 생성
	for (int i = 0; i < 2; i++) { // 0번 사람과 1번 사람
		pos[i][0] = 0; // 0의 시간엔 그자리 그대로 있다.
		for (int j = 1; j <= M; j++)
			cin >> pos[i][j]; // i번사람이 j라는 시간에 이동하는 방향
	}
	bc.push_back({ 0,0,500,0 }); // 충전기 사용 X, (모든좌표에서 고를 수 있는 선택지)
	for (int i = 0; i < A; i++) {
		int row, col, range, P;
		cin >> col >> row >> range >> P;
		bc.push_back({ row, col, range, P });
	}
}

int dr[] = { 0,-1,0,1,0 };
int dc[] = { 0,0,1,0,-1 };
void makeGraph(int time, int who, int row, int col) { // 시간별로 겹치는 영역들 찾기
	// time이라는 시간에 who라는 사람이 row,col에 있다.
	if (time > M)
		return;
	// 이동하기
	int nr = row + dr[pos[who][time]];
	int nc = col + dc[pos[who][time]];
	for (int i = 0; i <= A; i++) {
		BC nowbc = bc[i];
		int dist = abs(nowbc.row - nr) + abs(nowbc.col - nc);
		if (dist <= nowbc.range)
			// nowbc를 충전 가능 <- who라는 사람이 time이라는 시간에 nowbc를 충전 가능
			graph[who][time].push_back(i);
	}
	makeGraph(time + 1, who, nr, nc); // 다음 시간으로 가라!
}

int calcCharge(int time) {
	if (time > M) return 0;
	int maxCharge = 0;
	for (int i = 0; i < graph[0][time].size(); i++) {
		for (int j = 0; j < graph[1][time].size(); j++) {
			int A = graph[0][time][i];
			int B = graph[1][time][j];
			if (A == B) {
				maxCharge = max(maxCharge, bc[A].P);
			}
			else {
				maxCharge = max(maxCharge, bc[A].P + bc[B].P);
			}
		}

	}
	int nextCharge = calcCharge(time + 1);
	return maxCharge + nextCharge;
}


int solution() {
	makeGraph(0, 0, 1, 1);
	makeGraph(0, 1, 10, 10);
	return calcCharge(0);
}




int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		init();
		input();
		int ans = solution();
		cout << "#" << i + 1 <<" "<< ans << endl;
	}

}