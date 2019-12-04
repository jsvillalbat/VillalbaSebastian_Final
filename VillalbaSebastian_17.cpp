#include <iostream>
#include <fstream>
#include <cmath>
#include "stdio.h"

void init(double *psi, double delta_x, int n_x);
void print(double *psi, int n_x);
void copy(double *recibe, double *entrega, int n_x);
//void evolve_first(double *psi_future, double *psi_present, double *psi_past, double delta_t, double delta_x, double c, int n_x);
void evolve(double *psi_present, double *psi_past, double delta_t, double delta_x,int n_x);

int main(int argc, char **argv){
  double *psi_past = NULL;
  double *psi_present = NULL;
  //double *psi_future = NULL;
  double t_max=0.5;
  double delta_t=0.01;
  double delta_x=0.01;
  int n_x = 2/delta_x;
  int n_t = 0.5/delta_t;

  psi_past  = new double [n_x];
  psi_present  = new double [n_x];
  //psi_future  = new double [n_x];

  init(psi_past, delta_x, n_x);
  //init(psi_present, delta_x, n_x);

  print(psi_past, n_x);
  //evolve_first(psi_future, psi_present, psi_past, delta_t, delta_x, c, n_x);  
  //print(psi_present, n_x);

  for(int n=1;n<n_t-1;n++)
  {
    evolve(psi_present, psi_past, delta_t, delta_x, n_x);  
    print(psi_present, n_x);
    copy(psi_past, psi_present, n_x);
    //copy(psi_present, psi_future, n_x);
  }

  return 0;
}


void init(double *psi, double delta_x, int n_x){
  int i;
  for(i=0;i<n_x;i++){
      double dx = i*delta_x;
    psi[i] = exp((-0.5 *(dx-1)*(dx-1))/(0.25*0.25));
  }
}

void evolve(double *psi_present, double *psi_past, double delta_t, double delta_x,int n_x){
  int i;
  double c_prime = delta_x/delta_t;
  for(i=1;i<n_x-1;i++){
    psi_present[i] = psi_past[i] + c_prime*(psi_past[i+1] + psi_past[i]);
  }  
}


void copy(double *recibe, double *entrega, int n_x){
  int i;
  for (i=0;i<n_x;i++){
    recibe[i] = entrega[i];
  }
}



void print(double *psi, int n_x){
  int i;
  for(i=0;i<n_x;i++){
    std::cout << psi[i] << " ";
  }
  std::cout << "\n";
}