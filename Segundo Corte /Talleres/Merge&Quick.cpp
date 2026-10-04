#include <iostream>
#include <vector>
#include <chrono>

using namespace std;

// Estructura para registrar los resultados de rendimiento 📊
struct MetricasAlgoritmo {
    long long comparaciones;
    long long intercambios;
    double tiempo_segundos;
};

long long comparaciones_merge = 0;
long long intercambios_merge = 0;

vector<int> mezclar_subarreglos(const vector<int>& izquierda, const vector<int>& derecha) {
    vector<int> resultado;
    size_t i = 0, j = 0;

    while (i < izquierda.size() && j < derecha.size()) {
        comparaciones_merge++;
        if (izquierda[i] <= derecha[j]) {
            resultado.push_back(izquierda[i]);
            i++;
        } else {
            resultado.push_back(derecha[j]);
            j++;
        }
        intercambios_merge++; 
    }

    while (i < izquierda.size()) {
        resultado.push_back(izquierda[i]);
        i++;
    }
    while (j < derecha.size()) {
        resultado.push_back(derecha[j]);
        j++;
    }

    return resultado;
}

vector<int> merge_sort_recursivo(vector<int> datos) {
    if (datos.size() <= 1) {
        return datos;
    }

    size_t punto_medio = datos.size() / 2;
    vector<int> izquierda(datos.begin(), datos.begin() + punto_medio);
    vector<int> derecha(datos.begin() + punto_medio, datos.end());

    izquierda = merge_sort_recursivo(izquierda);
    derecha = merge_sort_recursivo(derecha);

    return mezclar_subarreglos(izquierda, derecha);
}

MetricasAlgoritmo ejecutar_merge_sort(const vector<int>& datos_originales) {
    comparaciones_merge = 0;
    intercambios_merge = 0;

    auto inicio = chrono::high_resolution_clock::now();
    vector<int> datos_ordenados = merge_sort_recursivo(datos_originales);
    auto fin = chrono::high_resolution_clock::now();

    chrono::duration<double> duracion = fin - inicio;
    return {comparaciones_merge, intercambios_merge, duracion.count()};
}

long long comparaciones_quick = 0;
long long intercambios_quick = 0;

int particion_hoare(vector<int>& arreglo, int bajo, int alto) {
    int pivote = arreglo[bajo];
    int i = bajo - 1;
    int j = alto + 1;

    while (true) {
        do {
            i++;
            comparaciones_quick++;
        } while (arreglo[i] < pivote);

        do {
            j--;
            comparaciones_quick++;
        } while (arreglo[j] > pivote);

        if (i >= j) {
            return j;
        }

        swap(arreglo[i], arreglo[j]);
        intercambios_quick++;
    }
}

void quicksort_recursivo(vector<int>& arreglo, int bajo, int alto) {
    if (bajo < alto) {
        int punto_particion = particion_hoare(arreglo, bajo, alto);
        quicksort_recursivo(arreglo, bajo, punto_particion);
        quicksort_recursivo(arreglo, punto_particion + 1, alto);
    }
}

MetricasAlgoritmo ejecutar_quicksort_inplace(vector<int> datos_originales) {
    comparaciones_quick = 0;
    intercambios_quick = 0;

    auto inicio = chrono::high_resolution_clock::now();
    if (!datos_originales.empty()) {
        quicksort_recursivo(datos_originales, 0, datos_originales.size() - 1);
    }
    auto fin = chrono::high_resolution_clock::now();

    chrono::duration<double> duracion = fin - inicio;
    return {comparaciones_quick, intercambios_quick, duracion.count()};
}

int main() {

    vector<int> datos_desordenados = {38, 27, 43, 3, 9, 82, 10};

    MetricasAlgoritmo metricas_merge = ejecutar_merge_sort(datos_desordenados);
    MetricasAlgoritmo metricas_quick = ejecutar_quicksort_inplace(datos_desordenados);

    cout << "1. Caso Normal (7 elementos desordenados):" << endl;
    cout << "  • Merge Sort -> Comparaciones: " << metricas_merge.comparaciones
         << " | Movimientos: " << metricas_merge.intercambios
         << " | Tiempo: " << metricas_merge.tiempo_segundos << " s" << endl;

    cout << "  • Quicksort  -> Comparaciones: " << metricas_quick.comparaciones
         << " | Intercambios: " << metricas_quick.intercambios
         << " | Tiempo: " << metricas_quick.tiempo_segundos << " s" << endl;

    vector<int> datos_ordenados = {1, 2, 3, 4, 5, 6, 7, 8};

    MetricasAlgoritmo metricas_peor_caso = ejecutar_quicksort_inplace(datos_ordenados);

    cout << "\n2. Peor Caso Quicksort (Lista ordenada N = 8, pivote al inicio):" << endl;
    cout << "  • Quicksort -> Comparaciones: " << metricas_peor_caso.comparaciones
         << " | Intercambios: " << metricas_peor_caso.intercambios
         << " | Tiempo: " << metricas_peor_caso.tiempo_segundos << " s" << endl;

    return 0;
}