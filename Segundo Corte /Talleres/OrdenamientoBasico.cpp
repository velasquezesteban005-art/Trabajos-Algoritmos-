#include <iostream>
#include <vector>
#include <string>
#include <chrono>

using namespace std;

struct MetricasAlgoritmo {
    long long comparaciones;
    long long intercambios;
    double tiempo_segundos;
};

struct RegistroProyecto {
    int id;
    string titulo;
    int veces_prestado;
};

MetricasAlgoritmo ejecutar_bubble_sort_optimizado(vector<int> arreglo) {
    long long comparaciones = 0;
    long long intercambios = 0;
    int n = arreglo.size();

    auto inicio = chrono::high_resolution_clock::now();

    for (int i = 0; i < n - 1; ++i) {
        bool hubo_intercambio = false; 
        for (int j = 0; j < n - i - 1; ++j) {
            comparaciones++;
            if (arreglo[j] > arreglo[j + 1]) {
                swap(arreglo[j], arreglo[j + 1]);
                intercambios++;
                hubo_intercambio = true;
            }
        }
        
        if (!hubo_intercambio) {
            break;
        }
    }

    auto fin = chrono::high_resolution_clock::now();
    chrono::duration<double> duracion = fin - inicio;

    return {comparaciones, intercambios, duracion.count()};
}


MetricasAlgoritmo ejecutar_insertion_sort(vector<int> arreglo) {
    long long comparaciones = 0;
    long long intercambios = 0;
    int n = arreglo.size();

    auto inicio = chrono::high_resolution_clock::now();

    for (int i = 1; i < n; ++i) {
        int valor_actual = arreglo[i];
        int j = i - 1;

        while (j >= 0) {
            comparaciones++;
            if (arreglo[j] > valor_actual) {
                arreglo[j + 1] = arreglo[j];
                intercambios++;
                j--;
            } else {
                break;
            }
        }
        arreglo[j + 1] = valor_actual;
    }

    auto fin = chrono::high_resolution_clock::now();
    chrono::duration<double> duracion = fin - inicio;

    return {comparaciones, intercambios, duracion.count()};
}


void ordenar_registros_proyecto(vector<RegistroProyecto>& registros) {
    int n = registros.size();
    for (int i = 0; i < n - 1; ++i) {
        bool hubo_intercambio = false;
        for (int j = 0; j < n - i - 1; ++j) {
            if (registros[j].veces_prestado > registros[j + 1].veces_prestado) {
                swap(registros[j], registros[j + 1]);
                hubo_intercambio = true;
            }
        }
        if (!hubo_intercambio) break;
    }
}

int main() {

    vector<int> datos_ordenados = {1, 2, 3, 4, 5, 6, 7, 8};

    MetricasAlgoritmo bubble_ord = ejecutar_bubble_sort_optimizado(datos_ordenados);
    MetricasAlgoritmo insertion_ord = ejecutar_insertion_sort(datos_ordenados);

    cout << "1. Prueba con Lista YA ORDENADA (N = 8):" << endl;
    cout << "  • Bubble Sort Optimizado -> Comparaciones: " << bubble_ord.comparaciones 
         << " | Intercambios: " << bubble_ord.intercambios << endl;
    cout << "  • Insertion Sort         -> Comparaciones: " << insertion_ord.comparaciones 
         << " | Intercambios: " << insertion_ord.intercambios << endl;


    vector<int> datos_desordenados = {38, 27, 43, 3, 9, 82, 10};

    MetricasAlgoritmo bubble_des = ejecutar_bubble_sort_optimizado(datos_desordenados);
    MetricasAlgoritmo insertion_des = ejecutar_insertion_sort(datos_desordenados);

    cout << "\n2. Prueba con Lista DESORDENADA (N = 7):" << endl;
    cout << "  • Bubble Sort Optimizado -> Comparaciones: " << bubble_des.comparaciones 
         << " | Intercambios: " << bubble_des.intercambios << endl;
    cout << "  • Insertion Sort         -> Comparaciones: " << insertion_des.comparaciones 
         << " | Intercambios: " << insertion_des.intercambios << endl;

    // --- EXPERIMENTO 3: Registros del Proyecto ---
    vector<RegistroProyecto> mis_registros = {
        {101, "Estructuras de Datos", 15},
        {102, "Algoritmos en C++", 2},
        {103, "Base de Datos", 27},
        {104, "Redes de Computadoras", 8}
    };

    ordenar_registros_proyecto(mis_registros);

    cout << "\n3. Registros ordenados por 'veces_prestado':" << endl;
    for (const auto& reg : mis_registros) {
        cout << "  • ID: " << reg.id << " | Titulo: " << reg.titulo 
             << " | Veces prestado: " << reg.veces_prestado << endl;
    }

    return 0;
}