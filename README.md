# MapReduce-Matrix-Multiplication

## Aufgabenstellung & Implementierung
Ziel des Projektes war die Implementierung eines One-Pass-, sowie eines Two-Pass Algorithmus zur Multiplikation zweier Matrizen A (m x n) und B (n x p) mittels MapReduce. Die Implementierung erfolgte über Python-Scripte.

## Funktionsweise und Ausführung
Im Folgenden werden Matrix A (2x3) und Matrix B (3x4) zu Matrix C (2x4) über den Two-Pass-Algorithmus miteinander multipliziert. Die beiden Ausgangs-Matrizen werden im ersten Schritt randomisiert erzeugt. Jedes a_ij bzw b_ij der Matrizen A und B kann dabei einen Wert von 0 bis 99 annehmen.

```python mapper1.py 2 3 4 99 | python reducer1.py | python mapper2.py | python reducer2.py```

Das Äquivalent für die Ausführung des One-Pass-Algorithmus lautet folgendermaßen:

```python mapper.py 2 3 4 99 | python reducer.py``` 

In beiden Varianten wird die errechnete Matrix C in Key-Value Paaren ausgegeben. Wobei der Key jeweils die Koordinaten in Matrix C darstellt. Der Value stellt den eigentlichen Wert des im Key adressierten Feldes a_ij bzw b_ij dar. Beispielhaft sei das Ergebnis einer (2x4)-Matrix dargestellt:

```
[1, 2]  3918
[0, 2]  7239
[1, 3]  4946
[0, 3]  13131
[1, 1]  4712
[1, 0]  2512
[0, 1]  9247
[0, 0]  9290
```
