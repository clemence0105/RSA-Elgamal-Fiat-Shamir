%module bInt
%{
/* Includes the header in the wrapper code */
#include "bInt.h"
%}

/* Parse the header file to generate wrappers */
%include "bInt.h"
