#include <stdio.h>
#include <stdlib.h>

double alpha = 0.4807, beta = 0.02482, delta = 0.02756, 
			gama = 0.9272, kappa = 0.000, 
			lambda = 0.000; //these can be changed 
			in order to produce specific scenarios

double dxdt(double x, double y){
	
	return alpha*x-beta*x*y-kappa*x*x;
	
}

double dydt(double x, double y){

	return delta*x*y-gama*y-lambda*y*y;

}

void RK(double dt, double *px, double *py){

	double	kx1,
		ky1,
		kx2,
		ky2,
		kx3,
		ky3,
		kx4,
		ky4,
		A[2],x=*px,y=*py;

		kx1=dt*dxdt(x,y);
		ky1=dt*dydt(x,y);
		kx2=dt*dxdt(x+kx1/2,y+ky1/2);
		ky2=dt*dydt(x+kx1/2,y+ky1/2);
		kx3=dt*dxdt(x+kx2/2,y+ky2/2);
		ky3=dt*dydt(x+kx2/2,y+ky2/2);
		kx4=dt*dxdt(x+kx3,y+ky3);
		ky4=dt*dydt(x+kx3,y+ky3);
		x = x + (1.0/6.0)*(kx1 + 2*kx2 + 2*kx3 + kx4);
		y = y + (1.0/6.0)*(ky1 + 2*ky2 + 2*ky3 + ky4);
	
  		*px = x;
  		*py = y;
	
}

int main(){

	FILE * fp;
	int i, n=5000;
	float dt = 0.01;
	double x = 34.91, y = 3.857;

	fp = fopen("output.txt", "w");
	fprintf(fp, "number of steps is: %d\n", n);
	fprintf(fp, "time interval is: %f\n", dt);
	fprintf(fp, "initial prey pop: %f, initial predator population: 
	%f\n", x,y);
	fprintf(fp, "alpha = $%$f beta = %f delta = %f gamma = %f 
	kappa = %f lambda = %f\n", alpha,beta,delta,gama,kappa,lambda);
	fprintf(fp, "x pop, y pop, time\n");

	for(i=0;i<=n;i++){
	RK(dt, &x, &y);
	fprintf(fp,"\%f \%f \%f\n", x, y, dt*i);
	
	}

}
