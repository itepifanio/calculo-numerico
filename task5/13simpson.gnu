set xrange[-10:10]
set yrange[-10:10]

set style fill pattern 4
f(x) = x*sin(x)
g1(x) = x >= -5 && x <= -1.6666    ? -0.335672*x**2 - 0.301676*x +2.08884 : 0/0
g2(x) = x > -1.6666 && x <= 1.6666 ? (0.597252*(x-1.6666)+0)*(x+1.6666)+1.6589  : 0/0
g3(x) = x > 1.6666 && x <= 5       ? -0.335851*x**2+0.302972*x+2.08681        : 0/0

plot 0 lc 0, f(x), g1(x) with filledcurve y1=0 title 'g1(x)', g2(x) with filledcurve y1=0 title 'g2(x)', g3(x) with filledcurve y1=0 title 'g3(x)'