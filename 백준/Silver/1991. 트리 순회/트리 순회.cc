#include <iostream>
#include <vector>
#define MAX 100

using namespace std;

struct node {
	char left;
	char right;
};

vector<node> v(MAX);

void preOrder(char node) { // 전위 순회
	// root - left - right
	if (node == '.') return;

	cout << node;
	preOrder(v[node].left);
	preOrder(v[node].right);
}

void inOrder(char node) { // 중위 순회
	// left - root - right
	if (node == '.') return;

	inOrder(v[node].left);
	cout << node;
	inOrder(v[node].right);
}

void postOrder(char node) { // 후위 순회
	// left - right - root
	if (node == '.') return;

	postOrder(v[node].left);
	postOrder(v[node].right);
	cout << node;
}

int main() {
	int n;
	cin >> n;

	char rt, l, r;
	for (int i = 0; i < n; i++) {
		cin >> rt >> l >> r;
		v[rt].left = l;
		v[rt].right = r;
	}

	preOrder('A');
	printf("\n");

	inOrder('A');
	printf("\n");

	postOrder('A');

	return 0;
}