#include <string>
#include <vector>
#include <string>
using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    int s1 =0;
    int s2 =0;
    for (int i=0; i< num_list.size();i++){
        if (num_list[i]%2 ==0)
           s1 = s1*10 + num_list[i];
        else
            s2 = s2*10 + num_list[i];
    }
    answer = s1 +s2;
    return answer;
}