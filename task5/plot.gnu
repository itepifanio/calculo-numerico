set xrange[-10:10]
set yrange[-10:10]

set style fill pattern 4
f(x) = x*sin(x)
g1(x) = x >= -5     && x <= -3.3334 ?  2.4956*x+7.6835 : 0/0
g2(x) = x > -3.3334 && x <= -1.6668 ? 1.3767*x+3.9538  : 0/0
g3(x) = x > -1.6668 && x <= 0       ? -0.9953*x        : 0/0
g4(x) = x > 0       && x <= 1.6666  ? 0.9953*x         : 0/0
g5(x) = x > 1.6666  && x <= 3.332   ? -1.3747*x+3.9505 : 0/0
g6(x) = x > 3.332   && x <= 5       ? -2.4964*x+7.6874 : 0/0

plot 0 lc 0, f(x), g1(x) with filledcurve y1=0 title 'g1(x)', g2(x) with filledcurve y1=0 title 'g2(x)', g3(x) with filledcurve y1=0 title 'g3(x)', g4(x) with filledcurve y1=0 title 'g4(x)', g5(x) with filledcurve y1=0 title 'g5(x)', g6(x) with filledcurve y1=0 title 'g6(x)'

#set style fill pattern 4
#set terminal postscript
#set samples 1000
#set xrange[-1.000000:10.000000]
#set output "exemplo1-38simp2.eps"
#plot 0 lc 0, sin(2*x)*x, x >= 0.000000 && x <= 4.500000 ? 0.000000 + (x - 0.000000)*0.141120 + (x - 0.000000)*(x - 1.500000)*(-0.280357) + (x - 0.000000)*(x-1.500000)*(x-3.000000)*0.247127 : 0/0 with filledcurve y1=0 title 'I0', x >= 4.500000 && x <= 9.000000 ? 1.854533 + (x - 4.500000)*(-3.382647) + (x - 4.500000)*(x - 6.000000)*2.926793 + (x - 4.500000)*(x-6.000000)*(x-7.500000)*(-1.624850) : 0/0 with filledcurve y1=0 title 'I1'