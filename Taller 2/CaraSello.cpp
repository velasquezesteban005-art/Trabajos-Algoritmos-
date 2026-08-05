/******************************************************************************
Cara o Sello
*******************************************************************************/
#include <iostream>
#include <random>
#include <ctime>
using namespace std;

int main()
{
    mt19937 generador(time(0));
    uniform_int_distribution<int>moneda(1,2); // << Aqui >> 1 = Cara y 2 = Sello
    
    int eleccion, resultado;
    string jugardeNuevo;
    
    do {
        do{
            cout<< " Por favor elija una de las siguientes opciones "<<endl;
            cout<< " 1 = Cara\n" << " 2 = Sello\n";
            cin>> eleccion;
        }while (eleccion != 1 && eleccion != 2);
        
        resultado = moneda(generador);
        
        cout<< " La moneda cayo en: ";
            if (resultado == 1){
                cout<< " Cara";
            }else {
                cout<< " Sello";
            } cout<< endl;
            
        if (resultado == eleccion){
            cout<< " Muy bien, Ganaste!" <<endl;
        }
        else {
            cout<< " Has perdido"<<endl;
        }
        cout<< " Quieres seguir jugando? "<<endl;
        cin>> jugardeNuevo;
        
   }while (jugardeNuevo == "si"|| jugardeNuevo == "SI" || jugardeNuevo == "Si");
   
   cout<< "Gracias por Jugar!"<<endl;

    return 0;
}
