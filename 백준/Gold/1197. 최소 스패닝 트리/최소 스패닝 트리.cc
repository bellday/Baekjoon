#include<iostream>
#include<algorithm>
using namespace std;

struct Edge {
    int cost;
    int A, B;
    bool operator< (Edge right) {
        if (cost < right.cost) return true;
        if (cost > right.cost) return false;

        if (A < right.A) return true;
        if (A > right.A) return false;

        if (B < right.B) return true;
        if (B > right.B) return false;
        return false;
    }
};

Edge edges[100001];

int parent[100001];
// 번외2 Find함수
int Find(int A) {
    if (A == parent[A]) return A;
    return parent[A] = Find(parent[A]);
}
// 번외3 Union함수
void Union(int A, int B) {
    int rootA = Find(A);
    int rootB = Find(B);
    parent[rootA] = rootB;
}

int main() {
    int cntNode, cntEdge;
    cin >> cntNode >> cntEdge;
    for (int i = 0; i < cntEdge; i++)
    {
        int A, B, cost;
        cin >> A >> B >> cost;
        edges[i] = { cost, A, B };
    } // 1. Edge 저장

    // 2. Edge 정렬 : O(ElogE) == O(ElogV) <- Kruskal의 시간복잡도
    sort(edges, edges + cntEdge);


    // 번외1. parent 초기화
    for (int i = 1; i <= cntNode; i++)
        parent[i] = i;

    int sum = 0;
    // 3. Edge 연결 <- Union-Find
    for (int i = 0; i < cntEdge; i++) {
        Edge now = edges[i];

        // 이미 같은 그룹(연결)이면 무시
        if (Find(now.A) == Find(now.B)) continue;

        Union(now.A, now.B); // 실제 연결
        sum += now.cost;
    }
    cout << sum;
}