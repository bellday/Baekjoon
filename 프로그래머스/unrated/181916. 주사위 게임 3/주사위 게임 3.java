class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int num= 0;
        if ((a==b)&&(a==c)&&(a==d))
        {
            answer = 1111*a;
        }
        else if((a==b)&&(a==c)&&(a!=d))
        {
            answer = (10*a + d) * (10*a + d);
        }
    
        else if((a==b)&&(a==d)&&(a!=c))
        {
            answer = (10*a + c) * (10*a + c);
        }
        else if((a==c)&&(a==d)&&(a!=b))
        {
            answer = (10*a + b) * (10*a + b);
        }
        else if((b==c)&&(b==d)&&(b!=a))
        {
            answer = (10*b + a) * (10*b + a);
        }
        // 2개씩 같을 경우
        else if ((a==b)&&(c==d)&&(a!=c))
        {
            if( (a-c)>= 0)
            {
                num = a-c;
            }
            else
            {
                num = c-a;
            }
            answer = (a+c) * num;
        }
        
        else if ((a==c)&&(b==d)&&(a!=b))
        {
            if( (a-b)>= 0)
            {
                num = a-b;
            }
            else
            {
                num = b-a;
            }
            answer = (a+b) * num;
        }
        
        else if ((a==d)&&(c==b)&&(a!=b))
        {
            if( (a-c)>= 0)
            {
                num = a-c;
            }
            else
            {
                num = c-a;
            }
            answer = (a+c) * num;
        }
        // 두개가 같고 나머지 2개가 다른경우
        
        else if ((a==b)&&(a!=c)&&(a!=d)&&(c!=d))
        {
            answer = c*d;
        }
        
        else if ((a==c)&&(a!=b)&&(a!=d)&&(b!=d))
        {
            answer = b*d;
        }
        
        else if ((a==d)&&(a!=b)&&(a!=c)&&(b!=c))
        {
            answer = b*c;
        }
        
        else if ((b==c)&&(b!=a)&&(b!=d)&&(a!=d))
        {
            answer = a*d;
        }
        
        else if ((b==d)&&(b!=a)&&(b!=c)&&(a!=c))
        {
            answer = a*c;
        }
        else if ((c==d)&&(c!=a)&&(c!=b)&&(a!=b))
        {
            answer = a*b;
        }
        else
        {
            if ((b>a)&&(c>a)&&(d>a))
            {
                answer = a;
            }
            else if ((a>b)&&(c>b)&&(d>b))
            {
                answer = b;
            }
            else if ((a>c)&&(b>c)&&(d>c))
            {
                answer = c;
            }
            else if ((a>d)&&(c>d)&&(b>d))
            {
                answer = d;
            }
            
        }
        return answer;
    }
}