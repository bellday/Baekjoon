#include <string>
#include <vector>

using namespace std;

vector<int> solution(int start, int end) {
    vector<int> answer(end-start +1);
    int x= 0;
    for(int i =start; i<end+1;i++){
        answer[x] =i;
        x++;
    }
    
    return answer;
}