<h1 id="tarefa-1">Tarefa 1</h1>
<ol style="list-style-type: decimal">
<li>Considere a função <span class="math inline">\(f(x) = x^3 - 2x^2 - x + 2\)</span>. Plote em um mesmo gráfico:
<ul>
<li><span class="math inline">\(f(x)\)</span> com a legenda <strong>função cúbica</strong> no intervalo de x <span class="math inline">\([-1.5, 2.5]\)</span></li>
<li>a reta tangente no ponto <span class="math inline">\((1, f(1))\)</span> com a legenda <strong>reta tangente em x = 1</strong></li>
<li>4 pontos: <span class="math inline">\((1, f(1))\)</span>, a interseção entre a reta tangente e o eixo x, os dois pontos críticos (e as respectivas retas tangentes)</li>
<li>Adicione um grid, eixo x e eixo y.</li>
</ul></li>
<li>🔢 📏 Seja uma função <span class="math inline">\(f(x)\)</span>:
<ul>
<li>Partindo de um ponto conhecido da função, estime outros pontos de <span class="math inline">\(f(x)\)</span> no intervalo <span class="math inline">\([-6:6]\)</span> sabendo que:
<ul>
<li><span class="math inline">\(f(0) = 1\)</span> (o ponto conhecido)</li>
<li><span class="math inline">\(f&#39;(x) = cos(x) - x sen(x)\)</span></li>
</ul></li>
<li>Grave os pontos estimados em um arquivo e plote-os com\ plot arquivos.pts with lp, x*cos(x) + 1
<ul>
<li><span class="math inline">\(f(x) = x*cos(x) + 1\)</span>, mas utilizaremos essa informação apenas para comparar as estimativas de <span class="math inline">\(f(x)\)</span> com <span class="math inline">\(f(x)\)</span></li>
</ul></li>
<li>Plote em um mesmo gráfico a função <span class="math inline">\(f(x) = x cos(x) + 1\)</span> e sua aproximação pela série de taylor em torno de <span class="math inline">\(a = 0\)</span> <span class="math display">\[\sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (x-a)^n\]</span> sabendo que a k-ésima (<span class="math inline">\(k &gt; 0\)</span>) derivada é: <span class="math display">\[f^{(k)}(x) = (-1)^{\frac{k-1}{2}} kcos(x) + (-1)^{\frac{k+1}{2}} x sen(x)\]</span> para <span class="math inline">\(k\)</span> ímpar e <span class="math display">\[f^{(k)}(x) = (-1)^{\frac{k}{2}} ksen(x) + (-1)^{\frac{k}{2}} x cos(x)\]</span> para <span class="math inline">\(k\)</span> par
<ul>
<li>Observação: nos testes realizados pelo professor, o gnuplot comete <em>overflow</em> a partir de <span class="math inline">\(n \ge 13\)</span>.</li>
</ul></li>
</ul></li>
</ol>