// 최소 한개의 모음, 두개의 자음으로 구성
// C가지에 대해 출력
// 
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int L , C;
vector<string> MAP;
vector<string> rst;
void input() {
	cin >> L >> C;
	MAP = vector<string>(C);

	for (int i = 0; i < C; i++) {
		cin >> MAP[i];
	}
	sort(MAP.begin(), MAP.end());
}
bool checkVal(string str) {
	int aeiouCount = 0;
	int notaeiouCount = 0;
	for (int i = 0; i < str.size(); i++) {
		if (str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u')
			aeiouCount++;
		else
			notaeiouCount++;
	}
	if (aeiouCount >= 1 and notaeiouCount >=2)return true;
	else
		return false;
}

void solution(int level,int use, string Code) {
	if (level >= L) { // 기저조건
		if (checkVal(Code))
			rst.push_back(Code);
		return;
	}
	for (int i = use+1; i < MAP.size(); i++) {
		solution(level + 1, i, Code + MAP[i]);
	}
}
void printRST() {
	sort(rst.begin(), rst.end());
	for (int i = 0; i < rst.size(); i++) {
		cout << rst[i] << endl;
	}
}
int main() {
	input();
	solution(0,-1,"");
	printRST();
}