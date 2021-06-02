module wigner
  use, intrinsic :: iso_c_binding
  implicit none
contains

  ! c wrapper for w3js function below
  subroutine c_w3js(j1,j2,j3,m1,m2,m3,fact,w3j_val) bind(c)
    integer(c_int), intent(in) :: j1,j2,j3,m1,m2,m3
    real(c_double), intent(in), dimension(0:101) :: fact
    real(c_double), intent(out) :: w3j_val
    !write(*,*) j1,j2,j3,m1,m2,m3,fact
    w3j_val = w3js(j1,j2,j3,m1,m2,m3,fact)
  end subroutine c_w3js

  !----------------------------------------------------------------
  ! This function calculates the 3-j symbol
  ! J_i and M_i have to be twice the actual value of J and M
  ! originally from hazel maths.f90
  ! fact is array of read(kind=8) factorial numbers 0:301
  !----------------------------------------------------------------
  function w3js(j1,j2,j3,m1,m2,m3,fact)
    integer :: m1, m2, m3, j1, j2, j3
    integer :: ia, ib, ic, id, ie, im, ig, ih, z, zmin, zmax, jsum
    real(kind=8) :: w3js, cc, denom, cc1, cc2
    real(kind=8) :: fact(0:101)

    w3js = 0.d0
    if (m1+m2+m3 /= 0) return
    ia = j1 + j2
    if (j3 > ia) return
    ib = j1 - j2
    if (j3 < abs(ib)) return
    if (abs(m1) > j1) return
    if (abs(m2) > j2) return
    if (abs(m3) > j3) return

    jsum = j3 + ia
    ic = j1 - m1
    id = j2 - m2

    ie = j3 - j2 + m1
    im = j3 - j1 - m2
    zmin = max0(0,-ie,-im)
    ig = ia - j3
    ih = j2 + m2
    zmax = min0(ig,ih,ic)
    cc = 0.d0
    do z = zmin, zmax, 2
       denom = fact(z/2)*fact((ig-z)/2)*fact((ic-z)/2)*fact((ih-z)/2)*fact((ie+z)/2)*fact((im+z)/2)
       if (mod(z,4) /= 0) denom = -denom
       cc = cc + 1.d0/denom
    enddo

    cc1 = fact(ig/2)*fact((j3+ib)/2)*fact((j3-ib)/2)/fact((jsum+2)/2)
    cc2 = fact((j1+m1)/2)*fact(ic/2)*fact(ih/2)*fact(id/2)*fact((j3-m3)/2)*fact((j3+m3)/2)
    cc = cc * sqrt(1.d0*cc1*cc2)
    if (mod(ib-m3,4) /= 0) cc = -cc
    w3js = cc
    if (abs(w3js) < 1.d-8) w3js = 0.d0
    return
  end function w3js


  !!!!!!!!!!!!

end module
