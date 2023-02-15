### TaxiWay 🚕️

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
