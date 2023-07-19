#include<iostream>
#include<thread>
#include<stdlib.h>
#include<windows.h>

using namespace std;

double feed_rate,ext_rate=0.0000;
bool flag=true;

void calc_time(bool status){

    if(feed_rate>=100){
        flag=false;
    }
    else{flag=true;}

}

int task(bool status){
    while(status){
        if(feed_rate<=100)
        {Sleep(2000);
        cout<<"Signal:[EN] "<<1<<" ";}
        else{Sleep(2000);
        cout<<"Signal:[EN] "<<0<<" ";}
    }
    return 0;
}

void poll(){
    
    for(int i=0;i<120;i++){
        if(feed_rate<=100){
            feed_rate=feed_rate+2.1453;
            ext_rate=ext_rate+0.1453;
            cout<<"Extrusion rate: "<<ext_rate<<" ";
            cout<<"Feed rate: "<<feed_rate<<" ";;
            Sleep(1000);
        }}}

int main(){

    cout<<"Extruder getting started"<<endl;
    Sleep(2000);
    cout<<"Hot End ready with filament. Internals ready to poll"<<endl;
    Sleep(2000);
    //auto start_time=high_resolution_clock::now();


    std::thread t1(task,flag);
    std::thread t2(poll);
    std::thread t3(calc_time,flag);

    system("Pause>0");
}