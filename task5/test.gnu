set style fill pattern 4
set terminal postscript
set samples 1000
set xrange[-1.000000:10.000000]
set output "exemplo1-38simp2.eps"
plot 0 lc 0, sin(2*x)*x, x >= 0.000000 && x <= 4.500000 ? 0.000000 + (x - 0.000000)*0.141120 + (x - 0.000000)*(x - 1.500000)*(-0.280357) + (x - 0.000000)*(x-1.500000)*(x-3.000000)*0.247127 : 0/0 with filledcurve y1=0 title 'I0', x >= 4.500000 && x <= 9.000000 ? 1.854533 + (x - 4.500000)*(-3.382647) + (x - 4.500000)*(x - 6.000000)*2.926793 + (x - 4.500000)*(x-6.000000)*(x-7.500000)*(-1.624850) : 0/0 with filledcurve y1=0 title 'I1'