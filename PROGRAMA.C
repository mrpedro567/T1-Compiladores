#include <stdio.h>

int main() {
	// TMP
	int T4;
	int T3;
	int T2;
	bool T1;
	bool T0;

	char A [256] ;
	int B, D ;
	float C ;
	printf( "Digite B" );
	scanf("%d", &B);
	printf( "Digite A:" );
	scanf("%s", A);
	T0=B>2;
if(T0){
	T1=B<=4;
if(T1){
	printf( "B esta entre 2 e 4" );
}
}
	T2=1+B;
	B = T2;
	T3=2+B;
	B = T3;
	T4=3+B;
	B = T4;
	D = B;
	C = 5.0;
	printf( "\nB=\n" );
	printf( D );
	printf( "\n" );
	printf( C );
	printf( "\n" );
	printf( A );

	 return 0;
}