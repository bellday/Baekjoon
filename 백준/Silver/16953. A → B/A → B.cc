#include <iostream>
using namespace std;
int A, B;
void input() {
	cin >> A >> B;
}
void calc(int a, int b) {
	int cnt = 1;
	int impossible = 0;
	while (1) {
		if (b == 0) { 
			impossible = 1;
			break; 
		}

		else if (b == a) break;
		if (b % 10 == 3 or b % 10 == 5 or b % 10 == 7 or b % 10 == 9) {
			impossible = 1;
			break;
		}
		else if (b % 10 == 1) {
			b -= 1;
			b = b / 10;
			cnt++;
		}
		else if (b % 2 == 0) {
			b = b / 2;
			cnt++;
		}
	}
	if (impossible == 1) cout << -1;
	else
	cout << cnt;
}
int main (){
	input();
	calc(A,B);
}