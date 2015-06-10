linux:
	swig -c++ -python bInt.i
	g++ -fPIC -c bInt.cpp
	g++ -fPIC -c bInt_wrap.cxx -I/usr/include/python2.7
	g++ -shared bInt.o bInt_wrap.o -o _bInt.so
	rm bInt_wrap.o bInt_wrap.cxx bInt.o
	touch __init__.py
		
windows:
	swig -c++ -python bInt.i
	g++ -c bInt.cpp
	g++ -c bInt_wrap.cxx -IC:\Python27\include
	g++ bInt.o bInt_wrap.o -Ic:\python27\include -Lc:\python27\libs -lpython27 -shared -o _bInt.pyd

clear:
	rm *.py* && rm *.so