#include <iostream>
#include <vector>
using namespace std;


void bubbleSort(int arr[], int n, int &comparaciones, int &intercambios) {
    comparaciones = 0;
    intercambios = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++;
            if (arr[j] > arr[j + 1]) {
                intercambios++;
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void selectionSort(int arr[], int n, int &comparaciones, int &intercambios) {
    comparaciones = 0;
    intercambios = 0;
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            comparaciones++;
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        if (minIdx != i) {
            swap(arr[i], arr[minIdx]);
            intercambios ++;
        }
    }
}


void insertionSort(int arr[], int n, int &comparaciones, int & intercambios) {
    comparaciones = 0;
    intercambios = 0;
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
       
        while (j >= 0) {
            comparaciones++;
            if (arr[j] > key) {
                arr[j + 1] = arr[j];
                intercambios++;
                j--;
            } else {
                break; 
            }
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    int comp = 0, inter = 0;

    bubbleSort(arr, n, comp, inter);
    cout << "Bubble Sort - Comparaciones: " << comp << ", Intercambios: " << inter << endl;
    selectionSort(arr, n, comp, inter);
    cout << "Selection Sort - Comparaciones: " << comp << ", Intercambios: " << inter << endl;
    insertionSort(arr, n, comp, inter);
    cout << "Insertio Sort - Comparaciones: " << comp << ", Intercambios: " << inter << endl;
    return 0;
}