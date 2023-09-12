#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> Lines;

int getLine(int val) {
	int retval = 0;

	for (int i = 0; i < Lines.size(); i++) {
		retval += Lines[i] / val;
	}
	return retval;
}

int main() {
	long long ans = 0;
	
	
	int Size, amount;
	cin >> Size >> amount;
	Lines = vector<int>(Size);

	int Maxlength = 0;
	for (int i = 0; i < Size; i++) {
		cin >> Lines[i];
		if (Maxlength < Lines[i])
			Maxlength = Lines[i];
	}

	long long left = 1;
	long long right = Maxlength;

	while (left <= right) {
		long long mid = (left + right) / 2;
		int midAmount = getLine(mid);

		if (midAmount == amount) {
			ans = max(mid,ans);
			left = mid + 1;
		}
		else if (midAmount < amount) {
			right = mid - 1;
		}
		else if (midAmount > amount) {
			left = mid + 1;
			ans = max(mid,ans);
		}
	}
	cout << ans;
}