### TaxiWay 🚕️

#### Algorítimo escolhido 🏅️

O algorítimo escolhido foi o Algoritmo A* , um algoritmo para Busca de Caminho , uma combinação heurística do algorítimo Breadth First Search com a formalidade do Algoritmo de Dijkstra.
Seu funcionamento se da pela busca de caminhos em um grafo de um vértice inicial até um final.
Ele busca o caminho em um grafo de um vértice inicial até um vértice final. 

#### Divisão do código 🕺️

A branch principal (main) contém a implementação do algorítimo com as devidas implementações de teste. Mas recomenda-se fortementa a rodagem e a visualização do código contida na [branch Felipe](https://github.com/insper-classroom/taxi-driver-without-reinforcement-learning-taxiway/tree/Felipe), que possui uma `animação implementada com pygame` mostrando a busca do algorítimo em ação!

#### Configurações ⚙️

Instale as bibliotecas necessárias utilizando o comando:

```bash

pip install -r requirements.txt

```

#### Limitações do Código 📌️

O presente projeto não apresenta garantia de solução a partir de mapas com dimensões superiores a 20x20 , podendo não chegar a melhor configuração de caminho nessas situações. O mesmo também não possui preparo para resolver situações em que o agente está "preso" rodeado de paredes e sem possibilidade de movimentaç

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
