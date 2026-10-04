#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;

struct MetricasAlgoritmo {
    long long comparaciones;
    long long intercambios;
    double tiempo_segundos;
};

long long comparaciones_heap = 0;
long long intercambios_heap = 0;

void hundir_nodo_minimo(vector<int>& arreglo, int tamano_heap, int indice_actual) {
    int indice_menor = indice_actual;
    int hijo_izquierdo = 2 * indice_actual + 1;
    int hijo_derecho = 2 * indice_actual + 2;

 
    if (hijo_izquierdo < tamano_heap) {
        comparaciones_heap++;
        if (arreglo[hijo_izquierdo] < arreglo[indice_menor]) {
            indice_menor = hijo_izquierdo;
        }
    }


    if (hijo_derecho < tamano_heap) {
        comparaciones_heap++;
        if (arreglo[hijo_derecho] < arreglo[indice_menor]) {
            indice_menor = hijo_derecho;
        }
    }


    if (indice_menor != indice_actual) {
        swap(arreglo[indice_actual], arreglo[indice_menor]);
        intercambios_heap++;
        hundir_nodo_minimo(arreglo, tamano_heap, indice_menor);
    }
}

MetricasAlgoritmo ejecutar_heapsort_minimos(vector<int> arreglo) {
    comparaciones_heap = 0;
    intercambios_heap = 0;
    int n = arreglo.size();

    auto inicio = chrono::high_resolution_clock::now();

    for (int i = n / 2 - 1; i >= 0; i--) {
        hundir_nodo_minimo(arreglo, n, i);
    }


    for (int i = n - 1; i > 0; i--) {
        swap(arreglo[0], arreglo[i]);
        intercambios_heap++;
        hundir_nodo_minimo(arreglo, i, 0);
    }

    auto fin = chrono::high_resolution_clock::now();
    chrono::duration<double> duracion = fin - inicio;

    return {comparaciones_heap, intercambios_heap, duracion.count()};
}


pair<long long, long long> ordenamiento_insercion_subcubeta(vector<int>& cubeta) {
    long long comp = 0, inter = 0;
    int n = cubeta.size();

    for (int i = 1; i < n; ++i) {
        int valor_actual = cubeta[i];
        int j = i - 1;
        while (j >= 0) {
            comp++;
            if (cubeta[j] > valor_actual) {
                cubeta[j + 1] = cubeta[j];
                inter++;
                j--;
            } else {
                break;
            }
        }
        cubeta[j + 1] = valor_actual;
    }
    return {comp, inter};
}

MetricasAlgoritmo ejecutar_bucket_sort(const vector<int>& datos_originales, int cantidad_cubetas) {
    if (datos_originales.empty()) return {0, 0, 0.0};

    auto inicio = chrono::high_resolution_clock::now();

    int valor_minimo = *min_element(datos_originales.begin(), datos_originales.end());
    int valor_maximo = *max_element(datos_originales.begin(), datos_originales.end());

    if (valor_minimo == valor_maximo) {
        auto fin = chrono::high_resolution_clock::now();
        chrono::duration<double> duracion = fin - inicio;
        return {0, 0, duracion.count()};
    }

    double rango_cubeta = static_cast<double>(valor_maximo - valor_minimo) / cantidad_cubetas;
    vector<vector<int>> arreglo_cubetas(cantidad_cubetas);

    for (int numero : datos_originales) {
        int indice_cubeta = static_cast<int>((numero - valor_minimo) / rango_cubeta);
        if (indice_cubeta >= cantidad_cubetas) {
            indice_cubeta = cantidad_cubetas - 1;
        }
        arreglo_cubetas[indice_cubeta].push_back(numero);
    }

    long long comparaciones_totales = 0;
    long long intercambios_totales = 0;
    vector<int> resultado_final;

    for (auto& cubeta : arreglo_cubetas) {
        auto [comp_sub, inter_sub] = ordenamiento_insercion_subcubeta(cubeta);
        comparaciones_totales += comp_sub;
        intercambios_totales += inter_sub;
        resultado_final.insert(resultado_final.end(), cubeta.begin(), cubeta.end());
    }

    auto fin = chrono::high_resolution_clock::now();
    chrono::duration<double> duracion = fin - inicio;

    return {comparaciones_totales, intercambios_totales, duracion.count()};
}


int main() {

    mt19937 generador(42);
    uniform_int_distribution<int> distribucion(1, 100);
    vector<int> datos_experimento(50);
    for (int& num : datos_experimento) {
        num = distribucion(generador);
    }


    MetricasAlgoritmo metricas_heap = ejecutar_heapsort_minimos(datos_experimento);

    cout << "1. Resultados Heapsort (Min-Heap):" << endl;
    cout << "  • Comparaciones: " << metricas_heap.comparaciones 
         << " | Intercambios: " << metricas_heap.intercambios 
         << " | Tiempo: " << metricas_heap.tiempo_segundos << " s" << endl;

    MetricasAlgoritmo metricas_b5 = ejecutar_bucket_sort(datos_experimento, 5);
    MetricasAlgoritmo metricas_b50 = ejecutar_bucket_sort(datos_experimento, 50);

    cout << "\n2. Resultados Bucket Sort:" << endl;
    cout << "  • Con 5 cubetas  -> Comparaciones: " << metricas_b5.comparaciones 
         << " | Tiempo: " << metricas_b5.tiempo_segundos << " s" << endl;
         
    cout << "  • Con 50 cubetas -> Comparaciones: " << metricas_b50.comparaciones 
         << " | Tiempo: " << metricas_b50.tiempo_segundos << " s" << endl;

    return 0;
}