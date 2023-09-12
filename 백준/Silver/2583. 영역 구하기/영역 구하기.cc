#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Pos {
    int row;
    int col;
};

vector<vector<int>> Graph;
vector<vector<bool>> Visit;
int M, N, K;

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int bfs(int row, int col) {
    queue<Pos> Q;
    Q.push({ row, col });
    Visit[row][col] = true;
    int AreaSize = 1;

    while (!Q.empty()) {
        Pos now = Q.front();
        Q.pop();
        int R = now.row;
        int C = now.col;

        for (int i = 0; i < 4; i++) {
            int NextR = R + dr[i];
            int NextC = C + dc[i];

            if (NextR >= 0 && NextR < M && NextC >= 0 && NextC < N) {
                if (!Visit[NextR][NextC] && Graph[NextR][NextC] == 0) {
                    Visit[NextR][NextC] = true;
                    Q.push({ NextR, NextC });
                    AreaSize++;
                }
            }
        }
    }

    return AreaSize;
}

int main() {
    cin >> M >> N >> K;
    Graph = vector<vector<int>>(M, vector<int>(N, 0));
    Visit = vector<vector<bool>>(M, vector<bool>(N, false));

    for (int i = 0; i < K; i++) {
        int startX, startY, EndX, EndY;
        cin >> startX >> startY >> EndX >> EndY;

        for (int j = startY; j < EndY; j++) {
            for (int k = startX; k < EndX; k++) {
                Graph[j][k] = 1; // 못가는 곳 설정
            }
        }
    }

    vector<int> areas;

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (!Visit[i][j] && Graph[i][j] == 0) {
                int areaSize = bfs(i, j);
                areas.push_back(areaSize);
            }
        }
    }

    sort(areas.begin(), areas.end());

    cout << areas.size() << "\n";
    for (int i = 0; i < areas.size(); i++) {
        cout << areas[i] << " ";
    }

    return 0;
}
