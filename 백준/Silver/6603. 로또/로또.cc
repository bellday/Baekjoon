#include <iostream>
#include <vector>

using namespace std;

vector<int> numbers;
vector<int> result;
int k;

void backtrack(int index, int count) {
    if (count == 6) {
        for (int i = 0; i < 6; i++) {
            cout << result[i] << " ";
        }
        cout << "\n";
        return;
    }

    if (index == k) {
        return;
    }

    // 현재 숫자를 선택하는 경우
    result.push_back(numbers[index]);
    backtrack(index + 1, count + 1);
    result.pop_back();

    // 현재 숫자를 선택하지 않는 경우
    backtrack(index + 1, count);
}

int main() {
    while (true) {
        cin >> k;
        if (k == 0) {
            break;
        }

        numbers.resize(k);
        for (int i = 0; i < k; i++) {
            cin >> numbers[i];
        }

        backtrack(0, 0);
        cout << "\n";
    }

    return 0;
}
