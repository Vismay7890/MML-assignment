#include <stdio.h>
#include <math.h>
int main()
{
    int a[100],b[100],n,x;
    int dot = 0;
    float norm;
    printf("Enter the size of vector a::");
    scanf("%d",&n);
    printf("Enter the size of vector b::");
    scanf("%d",&x);
    fflush(stdin);
    for (int i = 1; i <= n; i++)
    {
        printf("Enter %d element:",i);
        scanf("%d",a);
    }
    fflush(stdin);
    for (int i = 1; i <= x; i++)
    {
        printf("Enter %d element:",i);
        scanf("%d",b);
    }
    for (int i = 1; i <= 4; i++)
    {
        dot = dot + (a[i]*b[i]);
        printf("Dot product is %d\n",dot);
    }
    for (int i = 1; i <= 4; i++)
    {
        norm = sqrt(a[i]+b[i]);
    printf(" norm is %f\n",norm);     
    }
    
    
    
    return 0;
}