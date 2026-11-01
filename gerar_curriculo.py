#!/usr/bin/env python3
"""Gera app/src/main/assets/conteudos/curriculo.json (pacote de conteúdos do NDJENGUE MATH).

Cada subtema: (id, título, gerador, lição, [exemplos resolvíveis pelo motor]).
As lições usam fórmulas entre $…$ (KaTeX). Os exemplos são entradas do motor matemático.
"""
import json, os, sys

def S(id, titulo, gerador, licao, exemplos):
    return {"id": id, "titulo": titulo, "gerador": gerador, "licao": licao, "exemplos": exemplos}

def T(id, titulo, descricao, icone, subtemas):
    return {"id": id, "titulo": titulo, "descricao": descricao, "icone": icone, "subtemas": subtemas}

def L(id, ciclo, nome, descricao, disciplinas):
    return {"id": id, "ciclo": ciclo, "nome": nome, "descricao": descricao, "disciplinas": disciplinas}

def D(id, nome, temas):
    return {"id": id, "nome": nome, "temas": temas}

niveis = [
  L("c1", "PRIMARIO", "1.ª Classe", "Primeiros números e contas", [D("c1-mat", "Matemática", [
    T("c1-num", "Números até 20", "Contar, ler e comparar números", "pin", [
      S("c1-num-1", "Contar e comparar", "add",
        "Contamos objectos um a um. Um número é **maior** quando representa mais objectos: $8 > 5$ e $3 < 7$.\n\nOs números seguem-se sempre pela mesma ordem: 1, 2, 3, … Cada número é o anterior mais 1.",
        ["5 + 1", "8 + 1"])]),
    T("c1-ops", "Adição e subtracção", "Juntar e retirar até 20", "add", [
      S("c1-ops-1", "Adição até 20", "add",
        "**Adicionar** é juntar. Se tens $3$ laranjas e recebes mais $4$, ficas com $3 + 4 = 7$.\n\nA ordem não altera a soma: $3 + 4 = 4 + 3$.",
        ["3 + 4", "9 + 6"]),
      S("c1-ops-2", "Subtracção até 20", "sub",
        "**Subtrair** é retirar. Se tens $9$ lápis e dás $4$, ficas com $9 - 4 = 5$.\n\nPara confirmar, faz a conta ao contrário: $5 + 4 = 9$.",
        ["9 - 4", "15 - 7"])])])]),
  L("c2", "PRIMARIO", "2.ª Classe", "Números até 100 e primeiras multiplicações", [D("c2-mat", "Matemática", [
    T("c2-ops", "Adição e subtracção até 100", "Contas com dezenas e unidades", "calculate", [
      S("c2-ops-1", "Somar dezenas e unidades", "add",
        "Num número como $47$, o $4$ vale $4$ dezenas ($40$) e o $7$ vale $7$ unidades.\n\nPara somar, juntam-se unidades com unidades e dezenas com dezenas: $47 + 25 = 72$.",
        ["47 + 25", "38 + 46"]),
      S("c2-ops-2", "Subtrair com empréstimo", "sub",
        "Quando as unidades de cima são menores, pede-se emprestada uma dezena: $52 - 18 = 34$.",
        ["52 - 18", "90 - 37"])]),
    T("c2-mul", "Introdução à multiplicação", "Somas de parcelas iguais", "grid", [
      S("c2-mul-1", "Multiplicar é somar parcelas iguais", "mul",
        "$3 \\times 4$ significa $3$ grupos de $4$: $4 + 4 + 4 = 12$.\n\nA ordem dos factores não altera o produto: $3 \\times 4 = 4 \\times 3$.",
        ["3 × 4", "5 × 2"])])])]),
  L("c3", "PRIMARIO", "3.ª Classe", "Tabuada, divisão e fracções simples", [D("c3-mat", "Matemática", [
    T("c3-mul", "Tabuada e multiplicação", "Tabuadas até 10", "grid", [
      S("c3-mul-1", "Tabuadas", "mul", "Saber a tabuada torna as contas rápidas. Exemplo: $7 \\times 8 = 56$.\n\nQualquer número vezes $1$ é ele próprio; vezes $0$ é $0$.", ["7 × 8", "6 × 9"])]),
    T("c3-div", "Divisão", "Repartir em partes iguais", "call_split", [
      S("c3-div-1", "Divisão exacta", "div",
        "**Dividir** é repartir em partes iguais. $12 : 3 = 4$ porque $4 \\times 3 = 12$.\n\nA divisão é a operação inversa da multiplicação.",
        ["12 : 3", "56 : 7"])]),
    T("c3-fra", "Fracções simples", "Metades, terços e quartos", "pie_chart", [
      S("c3-fra-1", "O que é uma fracção", "fraction_add",
        "Uma fracção $\\frac{a}{b}$ divide a unidade em $b$ partes iguais e toma $a$ delas.\n\n$\\frac{1}{2}$ é metade; $\\frac{1}{4}$ é um quarto. Fracções com o mesmo denominador somam-se pelos numeradores: $\\frac{1}{4} + \\frac{2}{4} = \\frac{3}{4}$.",
        ["1/4 + 2/4", "1/2 + 1/2"])])])]),
  L("c4", "PRIMARIO", "4.ª Classe", "Números grandes, decimais e medidas", [D("c4-mat", "Matemática", [
    T("c4-ops", "Operações com números grandes", "Algoritmos das quatro operações", "calculate", [
      S("c4-ops-1", "Multiplicação por dois algarismos", "mul", "Multiplica-se pelas unidades e pelas dezenas e somam-se os resultados: $23 \\times 14 = 23 \\times 10 + 23 \\times 4 = 322$.", ["23 × 14", "45 × 12"]),
      S("c4-ops-2", "Divisão com resto zero", "div", "Na divisão $144 : 12 = 12$, o dividendo é $144$, o divisor $12$ e o quociente $12$.", ["144 : 12", "625 : 25"])]),
    T("c4-dec", "Números decimais", "Décimas e centésimas", "decimal_increase", [
      S("c4-dec-1", "Somar decimais", "decimal", "Alinham-se as vírgulas: unidades com unidades, décimas com décimas. $2{,}5 + 1{,}25 = 3{,}75$.", ["2,5 + 1,25", "10,4 - 3,7"])]),
    T("c4-fra", "Fracções equivalentes", "Mesma quantidade, escrita diferente", "pie_chart", [
      S("c4-fra-1", "Simplificar fracções", "fraction_add", "Multiplicando ou dividindo numerador e denominador pelo mesmo número obtém-se uma fracção equivalente: $\\frac{2}{4} = \\frac{1}{2}$.", ["10/4", "6/8 + 1/8"])])])]),
  L("c5", "PRIMARIO", "5.ª Classe", "Fracções, decimais e percentagens", [D("c5-mat", "Matemática", [
    T("c5-fra", "Operações com fracções", "Adição, subtracção, multiplicação e divisão", "pie_chart", [
      S("c5-fra-1", "Adição e subtracção de fracções", "fraction_add",
        "Com denominadores diferentes, procura-se o **m.m.c.** dos denominadores e escrevem-se fracções equivalentes: $\\frac{1}{2} + \\frac{1}{3} = \\frac{3}{6} + \\frac{2}{6} = \\frac{5}{6}$.",
        ["1/2 + 1/3", "3/4 - 1/6"]),
      S("c5-fra-2", "Multiplicação e divisão de fracções", "fraction_mul",
        "Multiplicam-se numeradores e denominadores: $\\frac{2}{3} \\times \\frac{3}{5} = \\frac{6}{15} = \\frac{2}{5}$.\n\nPara dividir, multiplica-se pela **inversa**: $\\frac{2}{3} : \\frac{4}{9} = \\frac{2}{3} \\times \\frac{9}{4} = \\frac{3}{2}$.",
        ["2/3 × 3/5", "2/3 : 4/9"])]),
    T("c5-per", "Percentagens", "Partes de 100", "percent", [
      S("c5-per-1", "Calcular uma percentagem", "percent", "$25\\%$ significa $25$ em cada $100$, ou seja $\\frac{25}{100}$. Assim, $25\\%$ de $80$ é $\\frac{25}{100} \\times 80 = 20$.", ["25% de 80", "15% de 200"])]),
    T("c5-geo", "Geometria básica", "Perímetros e áreas", "square_foot", [
      S("c5-geo-1", "Perímetro e área do rectângulo", "",
        "O **perímetro** é a soma dos lados: $P = 2 \\times (c + l)$. A **área** de um rectângulo é $A = c \\times l$.\n\nUm rectângulo com $5$ m por $3$ m tem perímetro $2 \\times (5 + 3) = 16$ m e área $5 \\times 3 = 15$ m².",
        ["2 × (5 + 3)", "5 × 3"])])])]),
  L("c6", "PRIMARIO", "6.ª Classe", "Potências, divisores e ordem das operações", [D("c6-mat", "Matemática", [
    T("c6-pot", "Potências e ordem das operações", "Calcular expressões numéricas", "superscript", [
      S("c6-pot-1", "Potências", "power", "$a^n$ é o produto de $n$ factores iguais a $a$: $2^5 = 2 \\times 2 \\times 2 \\times 2 \\times 2 = 32$.", ["2^5", "3^4"]),
      S("c6-pot-2", "Ordem das operações", "order",
        "Primeiro **parênteses**, depois **potências**, depois **multiplicações e divisões**, e por fim **adições e subtracções**, da esquerda para a direita.\n\n$2 + 3 \\times 4 = 2 + 12 = 14$, mas $(2 + 3) \\times 4 = 20$.",
        ["2 + 3 × 4", "(2 + 3) × 4 - 2^3"])]),
    T("c6-div", "Divisores e múltiplos", "m.d.c., m.m.c. e números primos", "tag", [
      S("c6-div-1", "Máximo divisor comum", "mdc", "O **m.d.c.** de dois números é o maior número que divide ambos. Pelo algoritmo de Euclides: $\\text{m.d.c.}(12, 18) = 6$.", ["mdc(12; 18)", "mdc(84; 36)"]),
      S("c6-div-2", "Mínimo múltiplo comum", "mmc", "O **m.m.c.** é o menor múltiplo comum: $\\text{m.m.c.}(4, 6) = 12$. Usa-se para somar fracções.", ["mmc(4; 6)", "mmc(8; 12; 15)"]),
      S("c6-div-3", "Factores primos", "primes", "Um número **primo** só é divisível por $1$ e por si próprio. Todo o número se decompõe em factores primos: $360 = 2^3 \\times 3^2 \\times 5$.", ["decompor 360", "decompor 84"])])])]),
  L("c7", "SECUNDARIO_I", "7.ª Classe", "Números racionais e equações do 1.º grau", [D("c7-mat", "Matemática", [
    T("c7-int", "Números inteiros e racionais", "Operações com sinais", "exposure", [
      S("c7-int-1", "Regra dos sinais", "order", "Na multiplicação e divisão: sinais iguais dão **+**, sinais diferentes dão **−**. $(-3) \\times (-4) = 12$ e $(-12) : 3 = -4$.", ["-3 * -4", "-12 : 3 + 5"])]),
    T("c7-alg", "Expressões algébricas", "Letras que representam números", "functions", [
      S("c7-alg-1", "Termos semelhantes", "expand", "Termos semelhantes têm a mesma parte literal e somam-se pelos coeficientes: $3x + 2x - x = 4x$.", ["simplificar 3x + 2x - x", "2x + 3 para x = 4"]),
      S("c7-alg-2", "Propriedade distributiva", "expand", "$a(b + c) = ab + ac$. Por exemplo, $3(x + 2) = 3x + 6$.", ["desenvolver 3(x + 2)", "desenvolver 2(x - 5) + 4x"])]),
    T("c7-eq", "Equações do 1.º grau", "Encontrar o valor da incógnita", "balance", [
      S("c7-eq-1", "Resolver equações", "linear",
        "Uma equação é uma **balança em equilíbrio**. Para isolar $x$ faz-se o mesmo nos dois membros.\n\n$2x + 3 = 7 \\Leftrightarrow 2x = 4 \\Leftrightarrow x = 2$. Verifica-se substituindo: $2 \\times 2 + 3 = 7$.",
        ["2x + 3 = 7", "3x - 5 = x + 9"])])])]),
  L("c8", "SECUNDARIO_I", "8.ª Classe", "Polinómios, sistemas e estatística", [D("c8-mat", "Matemática", [
    T("c8-pol", "Polinómios e casos notáveis", "Desenvolver e factorizar", "functions", [
      S("c8-pol-1", "Casos notáveis", "expand", "$(a + b)^2 = a^2 + 2ab + b^2$, $(a - b)^2 = a^2 - 2ab + b^2$ e $(a + b)(a - b) = a^2 - b^2$.", ["desenvolver (x + 3)^2", "desenvolver (x + 2)(x - 2)"]),
      S("c8-pol-2", "Factorização", "factor", "Factorizar é escrever como produto. Primeiro põe-se em evidência o factor comum: $2x^2 - 8 = 2(x^2 - 4) = 2(x - 2)(x + 2)$.", ["factorizar 2x^2 - 8", "factorizar x^2 - 5x + 6"])]),
    T("c8-eq", "Equações com denominadores", "Desembaraçar de denominadores", "balance", [
      S("c8-eq-1", "Equações com fracções", "linear_frac", "Multiplicam-se ambos os membros pelo m.m.c. dos denominadores: $\\frac{x}{2} + \\frac{x}{3} = 5 \\Leftrightarrow 3x + 2x = 30 \\Leftrightarrow x = 6$.", ["x/2 + x/3 = 5", "2(x - 1) = 3(x + 2)"])]),
    T("c8-sis", "Sistemas de duas equações", "Substituição e Cramer", "join_inner", [
      S("c8-sis-1", "Sistemas 2×2", "system", "Um sistema tem duas equações e duas incógnitas. Pelo **método de substituição** isola-se uma incógnita e substitui-se na outra equação.", ["x + y = 5; x - y = 1", "2x + 3y = 13; 4x - y = 5"])]),
    T("c8-est", "Estatística", "Média, mediana e moda", "bar_chart", [
      S("c8-est-1", "Medidas de tendência central", "statistics", "A **média** é a soma dos valores a dividir pelo número de valores. A **mediana** é o valor central dos dados ordenados. A **moda** é o valor mais frequente.", ["média 2; 4; 4; 5; 7", "estatística 12; 15; 11; 15; 18; 20"])])])]),
  L("c9", "SECUNDARIO_I", "9.ª Classe", "Inequações, equações do 2.º grau e funções", [D("c9-mat", "Matemática", [
    T("c9-ineq", "Inequações do 1.º grau", "Intervalos de números reais", "compare_arrows", [
      S("c9-ineq-1", "Resolver inequações", "inequality", "Resolve-se como uma equação, mas **ao multiplicar ou dividir por um número negativo, o sinal inverte-se**. $-3x + 6 \\geq 0 \\Leftrightarrow x \\leq 2$.", ["2x + 1 > 5", "-3x + 6 >= 0"])]),
    T("c9-quad", "Equações do 2.º grau", "Fórmula resolvente", "ssid_chart", [
      S("c9-quad-1", "Fórmula resolvente", "quadratic",
        "Para $ax^2 + bx + c = 0$: calcula-se $\\Delta = b^2 - 4ac$ e $x = \\frac{-b \\pm \\sqrt{\\Delta}}{2a}$.\n\nSe $\\Delta > 0$ há duas soluções; se $\\Delta = 0$ uma; se $\\Delta < 0$ nenhuma solução real.",
        ["x^2 - 5x + 6 = 0", "2x^2 + 3x - 2 = 0"]),
      S("c9-quad-2", "Equações incompletas", "quadratic", "Se $c = 0$, põe-se $x$ em evidência: $x^2 - 3x = 0 \\Leftrightarrow x(x - 3) = 0$. Se $b = 0$, isola-se $x^2$: $x^2 = 4 \\Leftrightarrow x = \\pm 2$.", ["x^2 - 3x = 0", "x^2 - 4 = 0"])]),
    T("c9-fun", "Função afim", "Rectas no plano", "show_chart", [
      S("c9-fun-1", "Função afim", "function", "$f(x) = mx + b$ é uma recta: $m$ é o **declive** e $b$ a **ordenada na origem**. Se $m > 0$ a função é crescente.", ["f(x) = 2x - 4", "f(x) = -x + 3"])])])]),
  L("c10", "SECUNDARIO_II", "10.ª Classe", "Funções quadráticas, polinómios e trigonometria", [D("c10-mat", "Matemática", [
    T("c10-quad", "Função quadrática", "Parábolas, vértice e zeros", "ssid_chart", [
      S("c10-quad-1", "Estudo da parábola", "function", "O gráfico de $f(x) = ax^2 + bx + c$ é uma parábola com vértice em $x_v = -\\frac{b}{2a}$. Se $a > 0$ tem um mínimo; se $a < 0$, um máximo.", ["f(x) = x^2 - 4x + 3", "f(x) = -x^2 + 2x + 3"]),
      S("c10-quad-2", "Inequações do 2.º grau", "inequality", "Encontram-se os zeros e estuda-se o sinal pela concavidade: $x^2 - 5x + 6 > 0 \\Leftrightarrow x < 2 \\vee x > 3$.", ["x^2 - 5x + 6 > 0", "x^2 - 4 <= 0"])]),
    T("c10-pol", "Polinómios e regra de Ruffini", "Divisão por (x − a)", "functions", [
      S("c10-pol-1", "Regra de Ruffini", "factor", "Se $P(a) = 0$, então $(x - a)$ divide $P(x)$ (teorema do resto). As raízes racionais são da forma $\\pm\\frac{p}{q}$.", ["x^3 - 6x^2 + 11x - 6 = 0", "factorizar x^3 - x"])]),
    T("c10-trig", "Trigonometria", "Seno, cosseno e tangente", "change_history", [
      S("c10-trig-1", "Razões trigonométricas", "",
        "Num triângulo rectângulo: $\\operatorname{sen}\\alpha = \\frac{\\text{cateto oposto}}{\\text{hipotenusa}}$, $\\cos\\alpha = \\frac{\\text{cateto adjacente}}{\\text{hipotenusa}}$. Os ângulos no motor estão em **radianos** ($180° = \\pi$).",
        ["sen(pi/6)", "cos(pi/3) + sen(pi/2)"])])])]),
  L("c11", "SECUNDARIO_II", "11.ª Classe", "Matrizes, sistemas e limites", [D("c11-mat", "Matemática", [
    T("c11-mat", "Matrizes e determinantes", "Regra de Sarrus", "grid_on", [
      S("c11-mat-1", "Determinantes", "matrix_det", "Para $2 \\times 2$: $\\det = ad - bc$. Para $3 \\times 3$ usa-se a **regra de Sarrus**.", ["det [1 2; 3 4]", "det [2 0 1; 1 3 2; 1 1 2]"])]),
    T("c11-sis", "Sistemas de três equações", "Regra de Cramer", "join_inner", [
      S("c11-sis-1", "Regra de Cramer", "system", "Cada incógnita é o quociente entre o determinante com a coluna substituída pelos termos independentes e o determinante do sistema.", ["x + y + z = 6; x - y = -1; 2x + y - z = 1"])]),
    T("c11-lim", "Limites", "Comportamento perto de um ponto", "trending_flat", [
      S("c11-lim-1", "Limites e indeterminações", "limit", "Primeiro substitui-se. Se aparece $\\frac{0}{0}$, simplifica-se (ou aplica-se a regra de L'Hôpital). No infinito, conta o termo de maior grau.", ["limite de (x^2 - 4)/(x - 2) quando x tende para 2", "limite de (2x^2 + 1)/(x^2 - 3) quando x tende para infinito"])])])]),
  L("c12", "SECUNDARIO_II", "12.ª Classe", "Derivadas, primitivas e probabilidades", [D("c12-mat", "Matemática", [
    T("c12-der", "Derivadas", "Taxa de variação instantânea", "trending_up", [
      S("c12-der-1", "Regras de derivação", "derivative", "$(x^n)' = n x^{n-1}$, $(u + v)' = u' + v'$, $(uv)' = u'v + uv'$, $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$.", ["derivada de x^3 + 2x", "derivada de x^2 * sen(x)"])]),
    T("c12-int", "Primitivas e integrais", "Área sob uma curva", "area_chart", [
      S("c12-int-1", "Primitivas imediatas", "integral", "$\\int x^n\\,dx = \\frac{x^{n+1}}{n+1} + C$ para $n \\neq -1$; $\\int \\frac{1}{x}\\,dx = \\ln|x| + C$.", ["integral de 3x^2 + 2x", "integral de cos(x) + e^x"]),
      S("c12-int-2", "Integral definido", "definite", "Pelo teorema fundamental do cálculo: $\\int_a^b f(x)\\,dx = F(b) - F(a)$, onde $F$ é uma primitiva de $f$.", ["integral de x^2 de 0 a 2", "integral de sen(x) de 0 a pi"])]),
    T("c12-prob", "Combinatória e probabilidades", "Contar casos", "casino", [
      S("c12-prob-1", "Factorial e arranjos", "", "$n! = 1 \\times 2 \\times \\dots \\times n$ conta as maneiras de ordenar $n$ objectos. A probabilidade de um acontecimento é $\\frac{\\text{casos favoráveis}}{\\text{casos possíveis}}$.", ["5!", "3/6", "6!/(2! * 4!)"])])])]),
  L("uni", "UNIVERSITARIO", "Ensino Universitário", "Análise, Álgebra Linear e Estatística", [
    D("uni-am", "Análise Matemática I", [
      T("uni-am-lim", "Limites e continuidade", "Indeterminações e L'Hôpital", "trending_flat", [
        S("uni-am-lim-1", "Regra de L'Hôpital", "limit", "Se $\\lim f = \\lim g = 0$, então $\\lim \\frac{f}{g} = \\lim \\frac{f'}{g'}$ (quando este existe).", ["limite de sen(x)/x quando x tende para 0", "limite de (x^3 - 1)/(x - 1) quando x tende para 1"])]),
      T("uni-am-der", "Cálculo diferencial", "Regra da cadeia e derivadas de ordem superior", "trending_up", [
        S("uni-am-der-1", "Regra da cadeia", "derivative", "$(f(g(x)))' = f'(g(x)) \\cdot g'(x)$. Exemplo: $(\\ln(x^2 + 1))' = \\frac{2x}{x^2 + 1}$.", ["derivada de ln(x^2 + 1)", "derivada de e^(2x)"]),
        S("uni-am-der-2", "Derivadas de ordem superior", "derivative", "A segunda derivada é a derivada da derivada e estuda a concavidade.", ["derivada segunda de x^4", "derivada segunda de sen(x)"]),
        S("uni-am-der-3", "Estudo de funções", "function", "Com $f'$ encontram-se os pontos críticos (máximos e mínimos) e a monotonia.", ["f(x) = x^3 - 3x", "f(x) = x^3 - 6x^2 + 9x"])]),
      T("uni-am-int", "Cálculo integral", "Primitivas e integrais definidos", "area_chart", [
        S("uni-am-int-1", "Primitivas", "integral", "Linearidade: $\\int (af + bg) = a\\int f + b\\int g$. Para argumentos lineares: $\\int \\cos(ax + b)\\,dx = \\frac{\\operatorname{sen}(ax + b)}{a} + C$.", ["integral de cos(2x) + e^x", "integral de 1/(2x + 1)"]),
        S("uni-am-int-2", "Integral definido", "definite", "O valor exacto obtém-se com uma primitiva; o motor confirma-o pela regra de Simpson.", ["integral de x^3 - x de 0 a 2", "integral de e^x de 0 a 1"])])]),
    D("uni-al", "Álgebra Linear e Geometria Analítica", [
      T("uni-al-mat", "Matrizes", "Operações e inversa", "grid_on", [
        S("uni-al-mat-1", "Produto de matrizes", "", "$C = AB$ com $c_{ij} = \\sum_k a_{ik} b_{kj}$. Só existe se o número de colunas de $A$ for igual ao número de linhas de $B$.", ["[1 2; 3 4] * [5 6; 7 8]", "transposta [1 2 3; 4 5 6]"]),
        S("uni-al-mat-2", "Matriz inversa", "matrix_inv", "$A$ é invertível se e só se $\\det A \\neq 0$. Calcula-se por Gauss-Jordan: $[A \\mid I] \\to [I \\mid A^{-1}]$.", ["inversa [4 7; 2 6]", "inversa [1 2 0; 0 1 3; 1 0 1]"])]),
      T("uni-al-det", "Determinantes", "Laplace e Sarrus", "grid_4x4", [
        S("uni-al-det-1", "Teorema de Laplace", "matrix_det", "Desenvolve-se por uma linha: $\\det A = \\sum_j (-1)^{i+j} a_{ij} M_{ij}$.", ["det [1 0 2 1; 0 3 1 0; 2 1 0 1; 1 0 1 2]", "det [[1,2,3],[0,1,4],[5,6,0]]"])]),
      T("uni-al-sis", "Sistemas lineares", "Gauss e classificação", "join_inner", [
        S("uni-al-sis-1", "Classificação de sistemas", "system", "Pelo teorema de Rouché: o sistema é possível se $\\operatorname{car}(A) = \\operatorname{car}(A|b)$; determinado se, além disso, for igual ao número de incógnitas.", ["x + y + z = 6; x - y = -1; 2x + z = 5", "característica [1 2 3; 2 4 6; 1 0 1]"])])]),
    D("uni-pe", "Probabilidades e Estatística", [
      T("uni-pe-desc", "Estatística descritiva", "Dispersão", "bar_chart", [
        S("uni-pe-desc-1", "Variância e desvio padrão", "statistics", "Variância amostral: $s^2 = \\frac{\\sum (x_i - \\bar{x})^2}{n - 1}$; o desvio padrão é $s = \\sqrt{s^2}$.", ["estatística 2; 4; 4; 4; 5; 5; 7; 9", "desvio padrão 10; 12; 23; 23; 16; 23; 21; 16"])])]),
    D("uni-md", "Matemática Discreta", [
      T("uni-md-ar", "Aritmética dos inteiros", "Euclides e factorização", "tag", [
        S("uni-md-ar-1", "Algoritmo de Euclides", "mdc", "$\\text{mdc}(a, b) = \\text{mdc}(b, a \\bmod b)$, até o resto ser $0$.", ["mdc(1071; 462)", "decompor 1001"])])]),
    D("uni-mn", "Métodos Numéricos", [
      T("uni-mn-raiz", "Raízes de polinómios", "Métodos exactos e numéricos", "ssid_chart", [
        S("uni-mn-raiz-1", "Raízes reais", "quadratic", "Raízes racionais pela regra de Ruffini; as restantes por métodos numéricos iterativos (Durand–Kerner).", ["x^3 - 2x - 5 = 0", "x^2 - 2x - 1 = 0"])])]),
  ]),
]

pack = {"id": "ndjengue-math-curriculo", "versao": 1, "resumo": "Currículo da 1.ª classe ao Ensino Universitário", "niveis": niveis}

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "app", "src", "main", "assets", "conteudos", "curriculo.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    json.dump(pack, f, ensure_ascii=False, indent=1)
n = sum(len(t["subtemas"]) for l in niveis for d in l["disciplinas"] for t in d["temas"])
print(f"{out}: {len(niveis)} níveis, {n} subtemas")
# Exemplos para o teste do motor (todos têm de ser resolvidos e verificados)
ex = [e for l in niveis for d in l["disciplinas"] for t in d["temas"] for s in t["subtemas"] for e in s["exemplos"]]
res = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "math-engine", "src", "test", "resources", "exemplos_curriculo.txt")
os.makedirs(os.path.dirname(res), exist_ok=True)
open(res, "w", encoding="utf-8").write("\n".join(ex))
