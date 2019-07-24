#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>
#include <unistd.h>

#define pi 4.0*atan(1.0)

#define MaxNumberOfForces 20
#define NumberOfRealisations 10000

void RotMat(double ct, double st, double p, double answer[])
{
        answer[0] = cos(p)*ct;
        answer[1] = sin(p)*ct;
        answer[2] = -st;

        answer[3] = -sin(p);
        answer[4] = cos(p);
        answer[5] = 0.0;

        answer[6] = cos(p)*st;
        answer[7] = sin(p)*st;
        answer[8] = ct;
}



int main()
{
	int n, m, k;
	double costhetaR, sinthetaR, phiR;
	double costhetaL, sinthetaL, phiL;
	double xR, yR, zR;
	double FxL, FyL, FzL;
	double Fx, Fy, Fz;
	double Fx0, Fy0, Fz0;
	double Tx, Ty, Tz;
	double DD[9];
	double AverageForceMagnitude, AverageTorqueMagnitude, AverageCos;
	FILE *fff, *ggg, *hhh;

	srand( (unsigned) time(NULL) * getpid());

	fff = fopen("AverageForce.txt", "w");
	ggg = fopen("AverageTorque.txt", "w");
	hhh = fopen("AverageAngle.txt", "w");

	for(n=1; n<=MaxNumberOfForces; n++){

		AverageForceMagnitude = 0.0;
		AverageTorqueMagnitude = 0.0;
		AverageCos = 0.0;

		for(m=0; m<NumberOfRealisations; m++){

			Fx = 0.0; Fy = 0.0; Fz = 0.0;
			Tx = 0.0; Ty = 0.0; Tz = 0.0;

			for(k=1; k<=n; k++){

				costhetaR = 1.0 - 2.0*(double)rand() / ((double)RAND_MAX + 1.0);
				sinthetaR = sqrt(1.0-costhetaR*costhetaR);
				phiR = 2.0*pi*(double)rand() / ((double)RAND_MAX + 1.0);

				xR = sinthetaR*cos(phiR);
				yR = sinthetaR*sin(phiR);
				zR = costhetaR;

				RotMat(costhetaR,sinthetaR,phiR,DD);

				costhetaL = (double)rand() / ((double)RAND_MAX + 1.0);
				sinthetaL = sqrt(1.0-costhetaL*costhetaL);
				phiL = 2.0*pi*(double)rand() / ((double)RAND_MAX + 1.0);

				FxL = sinthetaL*cos(phiL);
				FyL = sinthetaL*sin(phiL);
				FzL = costhetaL;

				Fx0 = DD[0]*FxL + DD[3]*FyL + DD[6]*FzL;
				Fy0 = DD[1]*FxL + DD[4]*FyL + DD[7]*FzL;
				Fz0 = DD[2]*FxL + DD[5]*FyL + DD[8]*FzL;

				Fx += Fx0;
				Fy += Fy0;
				Fz += Fz0;

				Tx += yR*Fz0 - zR*Fy0;
				Ty += zR*Fx0 - xR*Fz0;
				Tz += xR*Fy0 - yR*Fx0;

			}

			AverageForceMagnitude += sqrt(Fx*Fx + Fy*Fy + Fz*Fz);
			AverageTorqueMagnitude += sqrt(Tx*Tx + Ty*Ty + Tz*Tz);
			AverageCos += (Fx*Tx + Fy*Ty + Fz*Tz)/(sqrt(Fx*Fx + Fy*Fy + Fz*Fz)*sqrt(Tx*Tx + Ty*Ty + Tz*Tz));
		}

		fprintf(fff, "%d %f\n",n, AverageForceMagnitude/NumberOfRealisations);
		fprintf(ggg, "%d %f\n",n, AverageTorqueMagnitude/NumberOfRealisations);
		fprintf(hhh, "%d %f\n",n, AverageCos/NumberOfRealisations);

	}

	fclose(fff);fclose(ggg);fclose(hhh);

}
