/**
 *  处理56个字符以内的字符串的获得md5
 **/
 #include <string.h>
 #include <stdio.h>
 #include <python2.6/Python.h>

typedef unsigned int uint32;
typedef unsigned char uint8;

#define A_GROUP 64
#define DEAL_MAX 56
#define RES_LEN 33
#define A 0x67452301
#define B 0xefcdab89
#define C 0x98badcfe
#define D 0x10325476

/*待处理数据的缓存*/
static uint8 buffer[A_GROUP];
/*处理结果的缓存*/
static char result[RES_LEN];

 #define GET_UINT32(n, buffer, i)\
 {\
    (n) = (uint32)((uint8*)buffer)[(i)] \
    | (((uint32)((uint8*)buffer)[(i) + 1]) << 8)\
    | (((uint32)((uint8*)buffer)[(i) + 2]) << 16)\
    | (((uint32)((uint8*)buffer)[(i) + 3]) << 24);\
 }

 #define PUT_UINT32(n, buffer, i)\
 {\
    ((uint8*)buffer)[(i)] = (uint8)(n & 0xFF);\
    ((uint8*)buffer)[(i)] = (uint8)((n >> 8) & 0xFF);\
    ((uint8*)buffer)[(i)] = (uint8)((n >> 16) & 0xFF);\
    ((uint8*)buffer)[(i)] = (uint8)((n >> 24) & 0xFF);\
 }

void md5(char *chars, int len)
{
    uint32 X[16];
    uint32 a = A;
    uint32 b = B;
    uint32 c = C;
    uint32 d = D;
    int i = 0;
    unsigned int bit_len;
    //进行预处理
    //printf("%d %s\n", len, chars);
    len = (len > DEAL_MAX) ? DEAL_MAX : len;
    bit_len = len << 3;
    memcpy(buffer, chars, len);
    if(len < DEAL_MAX)
        buffer[len] = 128;
    memset(buffer + len + 1, 0, A_GROUP - len - 1);
    memcpy(buffer + DEAL_MAX, (char*)&bit_len, 4);
    //printf("OK");
    for(; i < 16; i ++)
    {
        GET_UINT32(X[i], buffer, 4 * i);
        //printf("%d %lu\n", i, X[i]);
    }

 #define S(x,n) ((x << n) | ((x & 0xFFFFFFFF) >> (32 - n)))  
 #define P(a, b, c, d, k, s, t)\
 {\
    a += F(b,c,d) + X[k] + t; a = S(a,s) + b; \
 }
 /*第一轮*/
 #define F(x, y, z) ((x & y) | ((~x) & z))
    P( a, b, c, d,  0,  7, 0xd76aa478 );  
    P( d, a, b, c,  1, 12, 0xE8c7b756 );  
    P( c, d, a, b,  2, 17, 0x242070db );  
    P( b, c, d, a,  3, 22, 0xc1bdcEEE );  
    P( a, b, c, d,  4,  7, 0xF57c0FaF );  
    P( d, a, b, c,  5, 12, 0x4787c62a );  
    P( c, d, a, b,  6, 17, 0xa8304613 );  
    P( b, c, d, a,  7, 22, 0xFd469501 );  
    P( a, b, c, d,  8,  7, 0x698098d8 );  
    P( d, a, b, c,  9, 12, 0x8b44F7aF );  
    P( c, d, a, b, 10, 17, 0xFFFF5bb1 );  
    P( b, c, d, a, 11, 22, 0x895cd7bE );  
    P( a, b, c, d, 12,  7, 0x6b901122 );  
    P( d, a, b, c, 13, 12, 0xFd987193 );  
    P( c, d, a, b, 14, 17, 0xa679438E );  
    P( b, c, d, a, 15, 22, 0x49b40821 );
 #undef F
 /*第二轮*/
 #define F(x, y, z) ((x & z) | (y & (~z)))
    P( a, b, c, d,  1,  5, 0xF61E2562 );  
    P( d, a, b, c,  6,  9, 0xc040b340 );  
    P( c, d, a, b, 11, 14, 0x265E5a51 );  
    P( b, c, d, a,  0, 20, 0xE9b6c7aa );  
    P( a, b, c, d,  5,  5, 0xd62F105d );  
    P( d, a, b, c, 10,  9, 0x02441453 );  
    P( c, d, a, b, 15, 14, 0xd8a1E681 );  
    P( b, c, d, a,  4, 20, 0xE7d3Fbc8 );  
    P( a, b, c, d,  9,  5, 0x21E1cdE6 );  
    P( d, a, b, c, 14,  9, 0xc33707d6 );  
    P( c, d, a, b,  3, 14, 0xF4d50d87 );  
    P( b, c, d, a,  8, 20, 0x455a14Ed );  
    P( a, b, c, d, 13,  5, 0xa9E3E905 );  
    P( d, a, b, c,  2,  9, 0xFcEFa3F8 );  
    P( c, d, a, b,  7, 14, 0x676F02d9 );  
    P( b, c, d, a, 12, 20, 0x8d2a4c8a ); 
 #undef F
/*第三轮*/
 #define F(x, y, z) (x ^ y ^ z)
    P( a, b, c, d,  5,  4, 0xFFFa3942 );  
    P( d, a, b, c,  8, 11, 0x8771F681 );  
    P( c, d, a, b, 11, 16, 0x6d9d6122 );  
    P( b, c, d, a, 14, 23, 0xFdE5380c );  
    P( a, b, c, d,  1,  4, 0xa4bEEa44 );  
    P( d, a, b, c,  4, 11, 0x4bdEcFa9 );  
    P( c, d, a, b,  7, 16, 0xF6bb4b60 );  
    P( b, c, d, a, 10, 23, 0xbEbFbc70 );  
    P( a, b, c, d, 13,  4, 0x289b7Ec6 );  
    P( d, a, b, c,  0, 11, 0xEaa127Fa );  
    P( c, d, a, b,  3, 16, 0xd4EF3085 );  
    P( b, c, d, a,  6, 23, 0x04881d05 );  
    P( a, b, c, d,  9,  4, 0xd9d4d039 );  
    P( d, a, b, c, 12, 11, 0xE6db99E5 );  
    P( c, d, a, b, 15, 16, 0x1Fa27cF8 );  
    P( b, c, d, a,  2, 23, 0xc4ac5665 );  
 #undef F
 /*第四轮*/
 #define F(x, y, z) (y ^ (x | (~z)))
    P( a, b, c, d,  0,  6, 0xF4292244 );  
    P( d, a, b, c,  7, 10, 0x432aFF97 );  
    P( c, d, a, b, 14, 15, 0xab9423a7 );  
    P( b, c, d, a,  5, 21, 0xFc93a039 );  
    P( a, b, c, d, 12,  6, 0x655b59c3 );  
    P( d, a, b, c,  3, 10, 0x8F0ccc92 );  
    P( c, d, a, b, 10, 15, 0xFFEFF47d );  
    P( b, c, d, a,  1, 21, 0x85845dd1 );  
    P( a, b, c, d,  8,  6, 0x6Fa87E4F );  
    P( d, a, b, c, 15, 10, 0xFE2cE6E0 );  
    P( c, d, a, b,  6, 15, 0xa3014314 );  
    P( b, c, d, a, 13, 21, 0x4E0811a1 );  
    P( a, b, c, d,  4,  6, 0xF7537E82 );  
    P( d, a, b, c, 11, 10, 0xbd3aF235 );  
    P( c, d, a, b,  2, 15, 0x2ad7d2bb );  
    P( b, c, d, a,  9, 21, 0xEb86d391 );  
 #undef F
    a += A;
    b += B;
    c += C;
    d += D;
    for(i = 0; i < 4; i ++)
    {
        //printf("%02x", ((unsigned char*)&a)[i]);
        sprintf(result + 2 * i, "%02x", ((unsigned char*)&a)[i]);
    }
    printf("\n");
    for(i = 0; i < 4; i ++)
    {
        //printf("%02x", ((unsigned char*)&b)[i]);
        sprintf(result + 2 * i + 8, "%02x", ((unsigned char*)&b)[i]);
    }
    for(i = 0; i < 4; i ++)
    {
        //printf("%02x", ((unsigned char*)&c)[i]);
        sprintf(result + 2 * i + 16, "%02x", ((unsigned char*)&c)[i]);
    }
    for(i = 0; i < 4; i ++)
    {
        //printf("%02x", ((unsigned char*)&d)[i]);
        sprintf(result + 2 * i + 24, "%02x", ((unsigned char*)&d)[i]);
    }
}

/*封装为python*/
static PyObject*
wrap_md5(PyObject *self, PyObject* args)
{
    char *chars;
    if(!PyArg_ParseTuple(args, "s", &chars))
    {
        PyErr_SetString(PyExc_RuntimeError, "参数不合法");
        return NULL;
    }
    md5(chars, strlen(chars));
    return PyString_FromString(result);
}

static PyMethodDef
methods[] = 
{
    {"md5", wrap_md5, METH_VARARGS, "md5"},
    {NULL, NULL, 0, NULL},
};

PyMODINIT_FUNC
initMD5(void)
{
    Py_InitModule("MD5", methods);   
}






