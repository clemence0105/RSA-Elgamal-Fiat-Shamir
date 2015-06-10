#pragma once
#include <iostream>

#define BASE 1000000000
#define DIV_ON_ZERO 1

class bInt
{
public:
	bInt();
	bInt(const char* String);
	bInt(const bInt& RightHandValue);
	bInt(long long int RightHandValue);
	~bInt();

	char* GetString();
	char* __str__();
	char* __repr__();
	bool GetNumberFromFile(const char* FileName);
	bool SaveNumberToFile(const char* FileName);
	bool GetNumberFromBinFile(const char* FileName);
	bool SaveNumberInBinFile(const char* FileName);

    bool Odd(); // для быстрого возведения в степень


	bInt operator=(const bInt& RightHandValue);
    
	bInt operator+(const bInt& right) const;
	bInt operator-() const;
	bInt operator-(const bInt& right) const;
	bInt operator*(const bInt& right) const;
	bInt operator/(const bInt& right) const;
	bInt operator%(const bInt& right) const;
	bInt operator^(const bInt& right) const;


	bool operator>(const bInt& B);
	bool operator>=(const bInt& B);
	bool operator<(const bInt& B);
	bool operator<=(const bInt& B);
	bool operator==(const bInt& B);
	bool operator!=(const bInt& B);

    // перегрузка операторов для Python
	bInt operator+(const int& right) const;
	bInt operator-(const int& right) const;
	bInt operator*(const int& right) const;
	bInt operator/(const int& right) const;
	bInt operator%(const int& right) const;

	bool operator>(const int& B);
	bool operator>=(const int& B);
	bool operator<(const int& B);
	bool operator<=(const int& B);
	bool operator==(const int& B);
	bool operator!=(const int& B);


	friend std::ostream& operator<<(std::ostream &out, bInt A);
	friend std::istream& operator>>(std::istream &is, bInt &A);


private:
	//Т.к оператор new имеет ограничение на максимальный размер массива 0x7fffffff байт, поэтому тип у _size - int 
	int _size;
	unsigned int* _digits;
	int _sign;


	void _SetSize(int size);
	unsigned int & operator[](int i);
	unsigned int operator[](int i) const;
	void _Copy(const bInt &rhv);
	void _DelNeedlessZeros();
	long long int _Compare(const bInt& B);
	void _ShiftLeft(int s);

	bInt _Sum_and_Sub(const bInt& left, const bInt& right) const;
	bInt _Multiplication(const bInt A, const bInt B) const;
	bInt _Division(const bInt& A, const bInt& B, bInt &remainder) const;

    friend bInt RandomLen(int bitLen);
    friend bInt RandomRange(bInt max);
};
// генерация случайного числа заданной длинны
bInt RandomLen(int bitLen);

// генерация случайного числа, не превосходящего заданное
bInt RandomRange(bInt max);

bInt Pow(const bInt& A, const bInt& B, bInt& modulus);

void initRandom();