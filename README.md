# Python-Bombemyne 🎮💣

Jogo no estilo *Bomberman* desenvolvido em **Python** utilizando a biblioteca **Pygame**.

---

## 🛠️ Estrutura de Desenvolvimento

O projeto será desenvolvido seguindo as etapas abaixo:

1. **Mecânicas do jogo**
     - Objetivo: Construir o núcleo da jogabilidade.
   - Tarefas:
     - Configurar janela Pygame e loop principal.
     - Criar classe `Player` para movimentação (teclas de seta).
     - Implementar colisões básicas com paredes e obstáculos.
     - Desenvolver classe `Bomb` para lançar e explodir bombas.
     - Criar classe `Enemy` com IA simples (movimento randômico).
   - Critérios de Conclusão:
     - Jogador se move sem travamentos.
     - Bombas explodem e removem blocos destructíveis.
     - Inimigos percorrem o mapa aleatoriamente.

2. **Sonorização** 
    – inserção de efeitos sonoros e músicas.

3. **Texturização** 
    – aplicação de sprites, fundo e outros elementos gráficos.

4. **Testes gerais e finalização** 
    – verificação de bugs, otimizações e ajustes finais.

Os arquivos principais ficarão na pasta `code`. Quando uma versão estiver **estável e funcional**, será feito um backup da build.

---

## 📘 Padrão de Commits

Os commits seguirão o seguinte padrão de log:

Log X.YYY

### Regras:

- `X` será incrementado **apenas** quando uma fase completa do projeto for finalizada (ex: todas as mecânicas básicas prontas).
- `YYY` será incrementado a cada alteração feita durante a fase atual.
- A descrição deve ser **objetiva**, explicando o que foi **adicionado**, **modificado** ou **removido**.

### Exemplo o segundo commit

# Tamanhos dos sprites e tela

Os recursos do Minerman Adventure vêm todos em 32×32 pixels (é justamente esse o “32x32” do nome do asset pack). Isso significa que:
  Cada tile de terreno (bloco ou chão) deve ter 32×32 px.
  Sprites de personagem (jogador, inimigos, itens etc.) também ocupam uma célula de 32×32 px em cada quadro de animação.

Portanto, para que tudo encaixe certinho na sua grid, basta usar 32 px como unidade básica de tamanho. Por exemplo:
Tamanho dos blocos (tiles):
  Largura: 32 px
  Altura: 32 px

Tamanho dos personagens/itens/efeitos
  Cada frame de animação (personagem andando, explosão, item) ocupa também 32×32 px.

Resolução da tela (window size) A escolha exata de resolução depende de quantos tiles você quer exibir em coluna/linha. Basta multiplicar o número de tiles desejados por 32. Alguns exemplos comuns de grid para-inspired-Bomberman são:
  20 colunas × 15 linhas → 20 × 32 = 640 px de largura
  15 × 32 = 480 px de altura
  