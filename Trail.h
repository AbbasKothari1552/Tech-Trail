int riddle(int n)
{
    int result = 1, i;
 
    // loop from 2 to n to get the factorial
    for (i = 2; i <= n-1; i++) {
        result *= i;
    }
    return result;
}