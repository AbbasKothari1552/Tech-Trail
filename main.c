#include <stdio.h>
#include "Trail.h"

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    int ans [] = {5,4,3,2,1};
    
    riddle(arr, size);
    
    for (int i = 0; i < size; i++) {
        if(arr[i] != ans[i]) {
            printf("Testcases Failed\n");
            break;
        }
    }
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
