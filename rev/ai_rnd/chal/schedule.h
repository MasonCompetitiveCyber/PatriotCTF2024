#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define INPUT_LEN 32
#define SEED_LEN 32
#define OUTPUT_LEN 32

void mat_mul(unsigned char mat1[2][2], unsigned char mat2[2][2], unsigned int res[2][2])
{
    int i, j, k;
    for (i = 0; i < 2; i++)
    {
        for(j = 0; j < 2; j++)
        {
            res[i][j] = 0;
            for(k=0;k<2;k++)
            {
                res[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}

unsigned char det_scalar_mod(unsigned int mat[2][2])
{
    int det = (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0]);
    return (unsigned char) (abs(det) % 255);
}

unsigned char def(unsigned char c, unsigned char i)
{
	return (c * i) % 255;
}


/*
 Below is generated code
*/
unsigned char _0(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 169;
	m1[0][1] = c;
	m2[0][1] = i;
	m1[1][0] = c;
	m2[1][0] = c;
	m1[1][1] = i;
	m2[1][1] = 209;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char _1(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 111;
	m1[0][1] = i;
	m2[0][1] = i;
	m1[1][0] = 66;
	m2[1][0] = c;
	m1[1][1] = i;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char _2(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 18;
	m1[0][1] = c;
	m2[0][1] = 121;
	m1[1][0] = i;
	m2[1][0] = 252;
	m1[1][1] = 175;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char _3(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = c;
	m1[0][1] = 205;
	m2[0][1] = 68;
	m1[1][0] = 44;
	m2[1][0] = 73;
	m1[1][1] = i;
	m2[1][1] = 55;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char _4(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 17;
	m2[0][0] = 201;
	m1[0][1] = 201;
	m2[0][1] = 107;
	m1[1][0] = c;
	m2[1][0] = 201;
	m1[1][1] = i;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char _5(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 12;
	m2[0][0] = c;
	m1[0][1] = i;
	m2[0][1] = 234;
	m1[1][0] = 46;
	m2[1][0] = c;
	m1[1][1] = 218;
	m2[1][1] = 185;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char _6(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 189;
	m2[0][0] = 51;
	m1[0][1] = i;
	m2[0][1] = i;
	m1[1][0] = 25;
	m2[1][0] = i;
	m1[1][1] = c;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char _7(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 68;
	m1[0][1] = 133;
	m2[0][1] = 60;
	m1[1][0] = 174;
	m2[1][0] = c;
	m1[1][1] = 80;
	m2[1][1] = 196;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char _8(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = c;
	m1[0][1] = 54;
	m2[0][1] = 153;
	m1[1][0] = i;
	m2[1][0] = c;
	m1[1][1] = 43;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char _9(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 159;
	m1[0][1] = 57;
	m2[0][1] = i;
	m1[1][0] = c;
	m2[1][0] = i;
	m1[1][1] = 70;
	m2[1][1] = 213;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char underscore(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = c;
	m1[0][1] = 218;
	m2[0][1] = 196;
	m1[1][0] = 139;
	m2[1][0] = i;
	m1[1][1] = i;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char left_curly(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 163;
	m1[0][1] = 226;
	m2[0][1] = c;
	m1[1][0] = i;
	m2[1][0] = 199;
	m1[1][1] = i;
	m2[1][1] = 162;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char right_curly(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = c;
	m1[0][1] = 40;
	m2[0][1] = 30;
	m1[1][0] = 196;
	m2[1][0] = i;
	m1[1][1] = c;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char a(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = c;
	m1[0][1] = 230;
	m2[0][1] = c;
	m1[1][0] = i;
	m2[1][0] = i;
	m1[1][1] = i;
	m2[1][1] = 147;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char b(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 242;
	m1[0][1] = i;
	m2[0][1] = 87;
	m1[1][0] = i;
	m2[1][0] = 2;
	m1[1][1] = c;
	m2[1][1] = 87;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char c(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = i;
	m1[0][1] = i;
	m2[0][1] = 142;
	m1[1][0] = 38;
	m2[1][0] = i;
	m1[1][1] = 200;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char d(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 116;
	m2[0][0] = 248;
	m1[0][1] = c;
	m2[0][1] = 53;
	m1[1][0] = i;
	m2[1][0] = 217;
	m1[1][1] = c;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char e(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 105;
	m1[0][1] = 156;
	m2[0][1] = 44;
	m1[1][0] = i;
	m2[1][0] = c;
	m1[1][1] = 16;
	m2[1][1] = 152;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char f(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 151;
	m2[0][0] = i;
	m1[0][1] = 82;
	m2[0][1] = i;
	m1[1][0] = i;
	m2[1][0] = 21;
	m1[1][1] = 179;
	m2[1][1] = 197;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char g(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 166;
	m2[0][0] = 242;
	m1[0][1] = 228;
	m2[0][1] = 43;
	m1[1][0] = i;
	m2[1][0] = i;
	m1[1][1] = i;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char h(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 25;
	m1[0][1] = i;
	m2[0][1] = c;
	m1[1][0] = 104;
	m2[1][0] = 173;
	m1[1][1] = 83;
	m2[1][1] = 15;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char i(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 198;
	m1[0][1] = 160;
	m2[0][1] = 201;
	m1[1][0] = 109;
	m2[1][0] = 80;
	m1[1][1] = 163;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char j(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 251;
	m2[0][0] = 60;
	m1[0][1] = i;
	m2[0][1] = 232;
	m1[1][0] = i;
	m2[1][0] = c;
	m1[1][1] = i;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char k(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 198;
	m2[0][0] = 75;
	m1[0][1] = 75;
	m2[0][1] = 69;
	m1[1][0] = 139;
	m2[1][0] = c;
	m1[1][1] = c;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char l(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 28;
	m2[0][0] = 0;
	m1[0][1] = 250;
	m2[0][1] = 60;
	m1[1][0] = 117;
	m2[1][0] = i;
	m1[1][1] = c;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char m(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 159;
	m2[0][0] = 7;
	m1[0][1] = i;
	m2[0][1] = c;
	m1[1][0] = i;
	m2[1][0] = c;
	m1[1][1] = 39;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char n(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 13;
	m2[0][0] = 57;
	m1[0][1] = 91;
	m2[0][1] = 54;
	m1[1][0] = c;
	m2[1][0] = i;
	m1[1][1] = i;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char o(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = 177;
	m1[0][1] = 12;
	m2[0][1] = i;
	m1[1][0] = 188;
	m2[1][0] = 194;
	m1[1][1] = 75;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char p(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 193;
	m2[0][0] = 90;
	m1[0][1] = 161;
	m2[0][1] = i;
	m1[1][0] = 227;
	m2[1][0] = 82;
	m1[1][1] = 228;
	m2[1][1] = 190;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char q(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = 20;
	m1[0][1] = i;
	m2[0][1] = c;
	m1[1][0] = 106;
	m2[1][0] = c;
	m1[1][1] = c;
	m2[1][1] = 52;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char r(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = c;
	m1[0][1] = c;
	m2[0][1] = 25;
	m1[1][0] = c;
	m2[1][0] = c;
	m1[1][1] = 221;
	m2[1][1] = 105;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char s(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 27;
	m2[0][0] = 63;
	m1[0][1] = i;
	m2[0][1] = i;
	m1[1][0] = 39;
	m2[1][0] = i;
	m1[1][1] = 0;
	m2[1][1] = 41;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char t(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = i;
	m1[0][1] = 84;
	m2[0][1] = c;
	m1[1][0] = i;
	m2[1][0] = 218;
	m1[1][1] = 91;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char u(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = c;
	m1[0][1] = 33;
	m2[0][1] = 148;
	m1[1][0] = 149;
	m2[1][0] = 110;
	m1[1][1] = 233;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char v(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 167;
	m2[0][0] = 139;
	m1[0][1] = 206;
	m2[0][1] = c;
	m1[1][0] = i;
	m2[1][0] = i;
	m1[1][1] = c;
	m2[1][1] = 71;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char w(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 221;
	m1[0][1] = 167;
	m2[0][1] = i;
	m1[1][0] = c;
	m2[1][0] = 87;
	m1[1][1] = c;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char x(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 154;
	m1[0][1] = 111;
	m2[0][1] = 209;
	m1[1][0] = 148;
	m2[1][0] = 167;
	m1[1][1] = 155;
	m2[1][1] = 44;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char y(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 2;
	m2[0][0] = 56;
	m1[0][1] = 242;
	m2[0][1] = c;
	m1[1][0] = 126;
	m2[1][0] = c;
	m1[1][1] = 204;
	m2[1][1] = 64;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char z(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = i;
	m1[0][1] = i;
	m2[0][1] = 92;
	m1[1][0] = 204;
	m2[1][0] = 189;
	m1[1][1] = c;
	m2[1][1] = 221;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char A(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 58;
	m2[0][0] = 248;
	m1[0][1] = 102;
	m2[0][1] = c;
	m1[1][0] = c;
	m2[1][0] = c;
	m1[1][1] = c;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char B(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 44;
	m2[0][0] = c;
	m1[0][1] = i;
	m2[0][1] = c;
	m1[1][0] = c;
	m2[1][0] = 91;
	m1[1][1] = c;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char C(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 35;
	m2[0][0] = c;
	m1[0][1] = 51;
	m2[0][1] = 143;
	m1[1][0] = i;
	m2[1][0] = i;
	m1[1][1] = i;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char D(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 173;
	m2[0][0] = i;
	m1[0][1] = 21;
	m2[0][1] = i;
	m1[1][0] = 75;
	m2[1][0] = 194;
	m1[1][1] = i;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char E(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 212;
	m2[0][0] = i;
	m1[0][1] = i;
	m2[0][1] = i;
	m1[1][0] = 130;
	m2[1][0] = i;
	m1[1][1] = i;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char F(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 182;
	m2[0][0] = 78;
	m1[0][1] = c;
	m2[0][1] = c;
	m1[1][0] = 132;
	m2[1][0] = c;
	m1[1][1] = c;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char G(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 108;
	m2[0][0] = 102;
	m1[0][1] = 190;
	m2[0][1] = 133;
	m1[1][0] = c;
	m2[1][0] = i;
	m1[1][1] = 132;
	m2[1][1] = 124;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char H(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 156;
	m2[0][0] = i;
	m1[0][1] = c;
	m2[0][1] = i;
	m1[1][0] = 17;
	m2[1][0] = c;
	m1[1][1] = 95;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char I(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = i;
	m1[0][1] = 31;
	m2[0][1] = 104;
	m1[1][0] = 63;
	m2[1][0] = 240;
	m1[1][1] = 156;
	m2[1][1] = 237;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char J(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 69;
	m2[0][0] = 27;
	m1[0][1] = 56;
	m2[0][1] = 46;
	m1[1][0] = 27;
	m2[1][0] = c;
	m1[1][1] = 157;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char K(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 253;
	m2[0][0] = c;
	m1[0][1] = c;
	m2[0][1] = c;
	m1[1][0] = c;
	m2[1][0] = i;
	m1[1][1] = c;
	m2[1][1] = 183;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char L(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 32;
	m2[0][0] = i;
	m1[0][1] = 102;
	m2[0][1] = i;
	m1[1][0] = i;
	m2[1][0] = i;
	m1[1][1] = 234;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char M(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 73;
	m2[0][0] = 239;
	m1[0][1] = 4;
	m2[0][1] = 187;
	m1[1][0] = i;
	m2[1][0] = c;
	m1[1][1] = c;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char N(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = 181;
	m1[0][1] = 71;
	m2[0][1] = 1;
	m1[1][0] = c;
	m2[1][0] = c;
	m1[1][1] = i;
	m2[1][1] = 28;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char O(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 227;
	m1[0][1] = i;
	m2[0][1] = i;
	m1[1][0] = 113;
	m2[1][0] = c;
	m1[1][1] = 50;
	m2[1][1] = 13;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char P(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 237;
	m2[0][0] = c;
	m1[0][1] = i;
	m2[0][1] = c;
	m1[1][0] = i;
	m2[1][0] = 188;
	m1[1][1] = 27;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char Q(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = i;
	m1[0][1] = 36;
	m2[0][1] = 240;
	m1[1][0] = i;
	m2[1][0] = 191;
	m1[1][1] = i;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char R(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = 167;
	m1[0][1] = i;
	m2[0][1] = c;
	m1[1][0] = i;
	m2[1][0] = i;
	m1[1][1] = i;
	m2[1][1] = i;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char S(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 32;
	m2[0][0] = 148;
	m1[0][1] = c;
	m2[0][1] = 111;
	m1[1][0] = i;
	m2[1][0] = c;
	m1[1][1] = 108;
	m2[1][1] = 251;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char T(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 232;
	m2[0][0] = c;
	m1[0][1] = c;
	m2[0][1] = 173;
	m1[1][0] = i;
	m2[1][0] = 224;
	m1[1][1] = c;
	m2[1][1] = 110;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char U(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = c;
	m1[0][1] = 70;
	m2[0][1] = 34;
	m1[1][0] = 114;
	m2[1][0] = 219;
	m1[1][1] = 235;
	m2[1][1] = 197;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char V(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = i;
	m2[0][0] = i;
	m1[0][1] = 97;
	m2[0][1] = 35;
	m1[1][0] = 17;
	m2[1][0] = 142;
	m1[1][1] = 232;
	m2[1][1] = 11;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char W(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = i;
	m1[0][1] = 51;
	m2[0][1] = 204;
	m1[1][0] = 69;
	m2[1][0] = c;
	m1[1][1] = 135;
	m2[1][1] = c;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char X(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = c;
	m2[0][0] = c;
	m1[0][1] = i;
	m2[0][1] = c;
	m1[1][0] = 107;
	m2[1][0] = i;
	m1[1][1] = c;
	m2[1][1] = 117;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char Y(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 41;
	m2[0][0] = 32;
	m1[0][1] = 207;
	m2[0][1] = c;
	m1[1][0] = c;
	m2[1][0] = 86;
	m1[1][1] = 129;
	m2[1][1] = 232;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}
unsigned char Z(unsigned char c, unsigned char i){
	unsigned char m1[2][2];
	unsigned char m2[2][2];
	unsigned int res[2][2];
	m1[0][0] = 152;
	m2[0][0] = 175;
	m1[0][1] = 99;
	m2[0][1] = 143;
	m1[1][0] = c;
	m2[1][0] = c;
	m1[1][1] = 77;
	m2[1][1] = 171;
	mat_mul(m1, m2, res);
	return det_scalar_mod(res);
}

// Array of functions that take a char and int argument
// Only these chars we care about, the rest can be thrown in a default
// _, [0-9a-zA-Z], {, }, 
unsigned char (*schedule[])(unsigned char, unsigned char) = {
def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, def, _0, _1, _2, _3, _4, _5, _6, _7, _8, _9, def, def, def, def, def, def, def, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, def, def, def, def, underscore, def, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, left_curly, def, right_curly, def, def
};
