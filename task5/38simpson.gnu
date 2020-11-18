set xrange[-10:10]
set yrange[-10:10]

set style fill pattern 4
f(x) = x*sin(x)
g1(x) = x >= -5 && x <= 0 ? -0.0751864*x**3 - 1.08756*x**2 - 2.59922*x : 0/0
g2(x) = x >= 0 && x <= 5 ? 0.0754092*x**3 - 1.089*x**2 + 2.60086*x : 0/0

plot 0 lc 0, f(x), g1(x) with filledcurve y1=0 title 'g1(x)', g2(x) with filledcurve y1=0 title 'g2(x)'