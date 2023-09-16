#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
struct Data {
	string Name;
	int Day;
	int Month;
	int Year;
};
vector<Data> Vect;
int Size;

bool compare(Data D1, Data D2) {
	if (D1.Year > D2.Year) return true;
	if (D1.Year < D2.Year) return false;
	if (D1.Month > D2.Month) return true;
	if (D1.Month < D2.Month) return false;
	if (D1.Day > D2.Day) return true;
	if (D1.Day < D2.Day) return false;
	return false;
}

void input() {
	
	cin >> Size;
	
	for (int i = 0; i < Size; i++) {
		string N; int D, M, Y;
		cin >> N >> D >> M >> Y;
		Vect.push_back({ N,D,M,Y });
	}
}

void calc() {
	sort(Vect.begin(), Vect.end(), compare);
	cout << Vect[0].Name <<"\n";
	cout << Vect[Vect.size() - 1].Name;
}

int main() {
	input();
	calc();
}