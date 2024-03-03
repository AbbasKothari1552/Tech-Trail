void riddle(int arr[]) {
    int start = 0;
    int end = size - 1;
    
    while (start < end) {
        // Swap elements at start and end indices
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        
        // Move towards the center
        start++;
        end--;
    }
}