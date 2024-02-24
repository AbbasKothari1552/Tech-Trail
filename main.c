#include <stdio.h>
#include "Trail.h"

int main() {
    int ans1 = 5040,ans2 = 40320;

        if(riddle(7) == ans1 && riddle(8) == ans2){
           printf("Completed your 1 task\n");
           printf("Next Riddle: \n");
        }
        else {
            printf("Testcases Failed\n");
            // printf("Try Again\n");
        }
    return 0;
}