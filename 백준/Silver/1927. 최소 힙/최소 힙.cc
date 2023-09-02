#include <iostream>
#include <queue>
using namespace std;
priority_queue<int,vector<int>,greater<int>> PQ;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int Size;
	cin >> Size;

	for (int i = 0; i < Size; i++) {
		int InputNumber;
		cin >> InputNumber;

		if (InputNumber == 0) {
			if (PQ.empty()) {
				cout << 0 << "\n";
			}
			else {
				cout << PQ.top() << "\n";
				PQ.pop();
			}
		}
		else {
			
			PQ.push(InputNumber);
		}
	}
}