#include <string>
#include <vector>

using namespace std;

vector<int> solution(int start, int end) {
    vector<int> answer(end-start +1);
    int y= 0;
    for(int i =start; i<end+1;i++){
        answer[y] =i;
        y++;
    }
    
    return answer;
}