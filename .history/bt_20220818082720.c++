#include <stdio.h>

/*Tạo hàm nhập mảng 1 chiều trong C*/
void input_array(int array[], int length){
    for (short i = 0; i < length; i++) scanf("%d", &array[i]);
}

/*Tạo hàm xuất mảng 1 chiều trong C*/
void show_array(int array[], int length){
    for(short i = 0; i < length; i++)  printf("%d ", array[i]);  
    printf("\n");
}

int main(void){
    /*Nhập mảng 1 chiều trong c*/
    int n;
    printf(">>Nhap so phan tu: ");
    scanf("%d", &n);
 
    int array[n];
    printf(">>Nhap phan tu:\n");
    input_array(array, n);
    
    /*xuất mảng 1 chiều trong c*/ 
    printf(">>Mang vua nhap:\n"); 
    show_array(array, n);
}
