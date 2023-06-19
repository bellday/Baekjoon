#include <stdio.h>

int main()
{
    long long int n=0; int b=0;
    int cases=0; long long int cnt_cases=2;
    scanf("%lld %d", &n, &b);
    //printf("%d %d\n",n,b);
    for(cases=0;cases<b;cases++){
        cnt_cases*=2;
    }
    cnt_cases--;
    //printf("%lld\n",cnt_cases);
    if (cnt_cases >= n){
        printf("yes");
    }
    else{
        printf("no");
    }
}
