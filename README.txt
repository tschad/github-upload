
one fortran file for all necessary routines
--> bind all of the routines as necessary
one cython file that does the c to python bit with those routines
--> compile all and create the package with the ext modules as defined

voila!

Try for example to write a package for weiner coefficients.

To use the routines internally, do i need a bound and inbound version of the routine?


https://northstar-www.dartmouth.edu/doc/solaris-forte/manuals/fortran/prog_guide/11_cfort.html
https://www.fortran90.org/src/best-practices.html
https://www.fortran90.org/src/rosetta.html
