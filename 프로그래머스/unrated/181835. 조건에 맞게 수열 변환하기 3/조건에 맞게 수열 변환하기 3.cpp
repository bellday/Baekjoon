#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr, int k) {
    vector<int> answer;
    int size = arr.size();
    int temp;
    for (int i = 0; i< size; i++)
    {
        if (k%2 == 1)
        {
            temp = arr[i] * k;
            arr[i] = temp;
        }
        else
        {
            temp = arr[i] + k;
            arr[i] = temp;
        }
        answer.push_back(arr[i]);
    }
    //answer =arr;
    return answer;
}