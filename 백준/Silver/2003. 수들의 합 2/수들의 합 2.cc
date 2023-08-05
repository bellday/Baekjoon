#include <iostream>

using namespace std;

int n, m;
int count = 0;

int main() {
    cin >> n >> m;

    int a[10000 + 1] = { 0, };

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int start = 0, end = 0;
    int result = a[0];

    while (start <= end && end < n) {
        if (result < m) {
            end++;
            result += a[end];
        }
        else if (result == m) {
            ::count++;
            end++;
            result += a[end];
        }
        else if (result > m) {
            result -= a[start];
            start++;

            if (start > end) {
                end = start;
                result = a[start];
            }
        }
    }

    cout << ::count;
}