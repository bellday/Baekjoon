#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(string my_string, string is_prefix) {
    int answer = 1;
    for(int i =0; i< is_prefix.length();i++)
    {
        if(my_string[i] != is_prefix[i])
        {
            answer =0;
            break;
        }
    }
    if(my_string.length() < is_prefix.length())
        answer =0;
    return answer;
}