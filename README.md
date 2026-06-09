# Análise de dados: O Impacto Pós-Pandemia no Cinema Internacional 

## Sobre o Projeto
Este projeto foi desenvolvido para analisar como a economia do cinema mudou entre o cenário pré-pandemia (2015-2019) e o cenário pós-pandemia/mercado híbrido (2022-atualmente). A base de dados utilizada foi a *'The Ultimate 1Million Movies Dataset (TMDB + IMDb)'* extraída do Kaggle. A análise procura responder a cinco perguntas:

1-Quais os gêneros com mais chances de darem lucro no pós-pandemia?
2-Qual o comportamento dos filmes de orçamento médio (Mid-budget) durante o período pós-pandemia, em comparação ao período pré-pandemia?
3-O quanto os filmes de terror se destacam, levando em conta o ROI(Return on Investment)?
4-O quanto a pandemia e a curta janela de lançamento nos streamings afetou a bilheteria dos filmes pós-pandemia?
5-Filmes em língua não-inglesa estão quebrando barreiras de lucro?


## Tecnologias e Ferramentas Utilizadas
**Python (Pandas, Matplotlib e Seaborn):** Utilizado como ambiente de desenvolvimento (VS Code) para conectar ao banco de dados, manipular os DataFrames estruturados e originar gráficos.
* **SQL (SQLite):** Utilizado para a extração, filtragem com condições e agregação dos dados brutos através do ambiente VS Code.
* **Excel:** Utilizado para a estruturação das métricas financeiras e geração de gráficos.


## Principais Insights Encontrados
A análise dos dados encontrou as seguintes informações para cada uma das perguntas:

1. [**Predominância das animações, aventuras e ficções científicas**](grafico_generoXlucro_excel.png)
Estes gêneros lideram o ranking de lucro médio no pós-pandemia. Eles funcionam como blockbusters de "apelo familiar", atraindo o público em massa para as salas de cinema (experiência de tela grande) e justificando o valor do ingresso premium.
  
2. [**O Efeito Tesoura nos filmes de orçamento médio**](grafico_mid_budget.png)
O volume de lançamentos caiu ~21% e o custo de produção subiu para $40.3M, mas o lucro médio despencou ~26% (caindo para $53.4M). Ficou mais caro produzir e o retorno diminuiu, empurrando diversos desses filmes para o streaming.

3. [**Financeiramente falando, os filmes de terror são os mais seguros**](boxplot_terror.png)
O terror é o campeão indiscutível de ROI (Retorno sobre o Investimento). Com orçamentos extremamente baixos, esses filmes geram lucros massivos. A análise de distribuição (boxplot) prova que, mesmo comparado aos campeões de lucro médio, é o gênero com maior ROI médio e com mais chances de "furar a bolha" do sucesso.

4. [**A cicatriz da pandemia: diminuição do lucro global**](grafico_eras_cinema.png)
A bilheteria média global encolheu e a janela mais curta entre o cinema e o streaming mudou o hábito do consumidor. O mercado híbrido fatura menos por filme de forma geral, evidenciando que a indústria ainda não recuperou totalmente as margens financeiras do pré-pandemia.

5. [**O cinema internacional caminha ao seu ápice financeiro**](cinema_internacional.png)
Filmes em língua não-inglesa (como produções coreanas, japonesas e europeias) estão quebrando barreiras históricas. Impulsionados pela globalização dos streamings e maior aceitação de legendas, o lucro médio e o alcance global dessas produções atingiram níveis recordes.


## Conclusão

Os dados extraídos e analisados provam que a pandemia de COVID-19 não foi apenas uma crise passageira, mas sim o **catalisador de uma transformação estrutural e permanente na economia do cinema mundial**. 

O mercado cinematográfico atual tornou-se polarizado e altamente avesso ao risco:
* **A Morte do Meio de Campo:** O tradicional "filme de orçamento médio" (como dramas e comédias românticas) está perdendo espaço nas telas grandes devido ao esmagamento de suas margens de lucro. Eles deram lugar a um modelo bifocal: de um lado, superproduções familiares de altíssimo orçamento (Animações e Aventuras) e, do outro, apostas de baixo custo com retorno astronômico (Terror).
* **A Nova Fronteira Global:** Enquanto Hollywood enfrenta dificuldades para retomar as margens de lucro do período pré-pandemia devido a janelas de exibição mais curtas, o mercado internacional (língua não-inglesa) encontrou nos streamings e na globalização a engrenagem perfeita para quebrar barreiras culturais e atingir seu ápice financeiro.

Em suma, ir ao cinema virou um evento de luxo reservado para espetáculos visuais ou experiências coletivas de nicho. Para os profissionais de dados do entretenimento, o desafio já não é mais prever o sucesso de bilheteria pelos moldes antigos, mas sim entender como maximizar o ciclo de vida de uma obra dentro deste ecossistema híbrido entre as salas de cinema e as plataformas de streaming.
