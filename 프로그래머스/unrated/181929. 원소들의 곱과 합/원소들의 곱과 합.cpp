#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    int rst1=1;
    for (int i=0;i<num_list.size();i++)
    {
        rst1 *= num_list[i];
            answer+=num_list[i];
    }
    answer = answer*answer;
    if (rst1 > answer)
        return 0;
    else
        return 1;


}