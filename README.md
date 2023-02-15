### TaxiWay 🚕️

#### Algorítimo escolhido 🏅️

O algorítimo escolhido foi o Algoritmo A* , um algoritmo para Busca de Caminho , uma combinação heurística do algorítimo Breadth First Search com a formalidade do Algoritmo de Dijkstra.
Seu funcionamento se da pela busca de caminhos em um grafo de um vértice inicial até um final.
Ele busca o caminho em um grafo de um vértice inicial até um vértice final. 

#### Divisão do código 🕺️

A branch principal (main) contém a implementação do algorítimo com as devidas implementações de teste. Mas recomenda-se fortementa a rodagem e a visualização do código contida na [branch Felipe](https://github.com/insper-classroom/taxi-driver-without-reinforcement-learning-taxiway/tree/Felipe), que possui uma **animação implementada com pygame** mostrando da busca do algorítimo em ação!

#### Configurações ⚙️

Caso não posua pytest instalado, instale utilizando o comando:

```bash

pip install pytest

```

#### Formato input esperado 📌️

```bash
largura     altura

posicao de inicio  taxi (x,y)


posicao de inicio  passageiro (x,y)


posicao de iniio  destino (x,y)


X,X,X,X,X

X,T,0,0,X 

X,0,0,P,X 

X,D,0,0,X 

X,X,X,X,X  
```
Legenda :
```bash
0 -> Caminho livre

X -> Parede

T -> Taxi

P -> Person

D -> Destino

T+P -> Passageiro no Taxi

T+P+D -> (Passageiro + Taxi) no Destino
```

#### Rodagem do código 👩‍💻️

* Rodar testes:
```bash
pytest test.py
```
* Rodar algorítimo:
```bash
python main.py Data/grid{numero}.txt
```
