#include <iostream>
#include <map>
int DAT[20000000] = { 0 , };
using namespace std;
map<int, int> MAP;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
	int N, M;
	
	cin >> N;
	for (int i = 0; i < N; i++) {
		int input;
		cin >> input;
		DAT[10000000 + input] += 1;
	}
	cin >> M;
	for (int i = 0; i < M; i++) {
		int output;
		cin >> output;
		cout << DAT[10000000+output] << " ";
	}
	
}