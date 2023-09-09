#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> graph;
vector<vector<int>> visit;
int maxheight = 0;
int N;

void input() {
    cin >> N;
    graph = vector<vector<int>>(N, vector<int>(N));
    visit = vector<vector<int>>(N, vector<int>(N));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> graph[i][j];
            if (maxheight < graph[i][j])
                maxheight = graph[i][j];
        }
    }
}

void init() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            visit[i][j] = 0;
        }
    }
}

void bfs(int row, int col, int level) {
    int dr[4] = { -1, 1, 0, 0 };
    int dc[4] = { 0, 0, -1, 1 };
    queue<pair<int, int>> q;
    q.push({ row, col });
    visit[row][col] = 1;

    while (!q.empty()) {
        int r = q.front().first;
        int c = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nextrow = r + dr[i];
            int nextcol = c + dc[i];

            if (nextrow >= 0 && nextrow < N && nextcol >= 0 && nextcol < N
                && visit[nextrow][nextcol] == 0 && graph[nextrow][nextcol] > level) {
                visit[nextrow][nextcol] = 1;
                q.push({ nextrow, nextcol });
            }
        }
    }
}

int main() {
    input();
    int max_safe_area = 0;

    for (int i = 0; i <= maxheight; i++) {
        int safe_area = 0;
        init();

        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                if (visit[j][k] == 0 && graph[j][k] > i) {
                    bfs(j, k, i);
                    safe_area++;
                }
            }
        }

        max_safe_area = max(max_safe_area, safe_area);
    }

    cout << max_safe_area << endl;

    return 0;
}
