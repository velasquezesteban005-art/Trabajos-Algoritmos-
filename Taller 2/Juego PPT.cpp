// juego piedra papel o tijera //

#include <iostream>
#include <random>

using namespace std;

int main()
{
    int opcion, maquina;
    
    random_device rd;
    mt19937 gen (rd());
    uniform_int_distribution <> dist(1,3);
    
    cout << " Bienvenidos al juego PIEDRA PAPEL O TIJERA "<< endl;
    do {
        cout << " Por favor elija una de las siguientes opciones: "<< endl;
        cout << " 1. Piedra\n" << " 2. Papel\n" << " 3. Tijera\n";
        cin>> opcion;
        
        maquina = dist(gen);
        
        cout<< " La maquina eligio: " << maquina << endl;
        
        if (opcion == maquina){
            cout<< " Ha sido un empate, intentalo de nuevo "<< endl;
        }
        else if (( opcion == 1 && maquina == 3 ) || ( opcion == 2 && maquina == 1) || ( opcion == 3 && maquina == 2)){
            cout<< " Muy bien, Ganaste! "<<endl;
        } 
        else {
            cout<< " Has perdido! "<< endl;
        }
        
    }while ( opcion == maquina );   
        


    return 0;
}