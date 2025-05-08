# 🛡️ Detecção de Fraudes em Cenários de Cold Start

**Autor:** Daniel Victor Simões Neves  
**Finalidade:** Este projeto foi desenvolvido como uma prova de conceito prática e funcional para detectar fraudes em ambientes onde não há histórico anterior (Cold Start). O objetivo principal é demonstrar domínio em técnicas híbridas de detecção de fraude combinando regras de negócio, heurísticas e algoritmos de machine learning explicável.

---

## 🧠 Problema Resolvido

Sistemas antifraude frequentemente dependem de históricos longos para aprender padrões suspeitos. Mas como lidar com **novos cadastros ou transações sem histórico prévio**? Este projeto responde a esse desafio com uma abordagem **inteligente e transparente**, unindo:

- 📜 Regras baseadas em conhecimento de domínio (heurísticas)
- 🌲 Modelos supervisionados (Árvore de Decisão)
- 🧪 Modelos não supervisionados (Isolation Forest)
- 🔁 Aprendizado com feedback contínuo

---

## 🧩 Etapas do Projeto

### 1. Entendimento do Problema
- Identificamos sinais comuns em fraudes de primeiro acesso: e-mail temporário, IP anônimo, dispositivo novo, tempo de preenchimento rápido, localização suspeita.

### 2. Simulação de Dados
- Geramos 1.000 registros sintéticos representando cadastros com e sem fraude, permitindo testes controlados.

### 3. Regras de Negócio e Heurísticas
- Implementamos funções manuais para classificar o risco (baixo, médio, alto) com base em combinações suspeitas de sinais.
- Criamos um classificador de primeira camada com base em lógica de especialistas.

### 4. Machine Learning Não Supervisionado
- Usamos o Isolation Forest para detectar **anormalidades** em registros novos, mesmo sem saber se são fraudes.

### 5. Combinação de Regras + ML
- Mesclamos a decisão de risco com o score de anomalia, criando uma tabela final com 3 categorias:
    - ✅ Aprovar
    - 🧐 Revisar
    - ❌ Rejeitar

### 6. Simulação de Feedback e Aprendizado
- Simulamos correções manuais nas previsões erradas e reprocessamos o modelo para aprender com erros e melhorar seu desempenho.

---

## 📊 Resultados Obtidos

| Métrica                          | Antes do Feedback | Após Feedback |
|----------------------------------|-------------------|---------------|
| **Acurácia Total**               | 77.30%            | 78.10%        |
| **Falsos Positivos (FP)**        | 1.79%             | 0.00%         |
| **Falsos Negativos (FN)**        | 18.72%            | Reduzido      |

- A integração entre lógica humana e machine learning resultou em um sistema robusto e explicável.
- A visualização das decisões finais mostrou como os scores influenciam as ações de aprovação, revisão ou rejeição.

---

## 🛠️ Técnicas Utilizadas

- **Geração de dados sintéticos**
- **Regras de negócio em Python**
- **Árvore de Decisão (scikit-learn)**
- **Isolation Forest**
- **Avaliação com matriz de confusão e métricas**
- **Simulação de feedback supervisionado**
- **Visualizações com Seaborn e Matplotlib**

---

## 🔍 Relevância para Recrutadores

Este projeto demonstra capacidade de:

✅ Trabalhar com cenários de dados escassos (cold start)  
✅ Combinar conhecimento de domínio com aprendizado de máquina explicável  
✅ Desenvolver soluções interpretáveis e ajustáveis a problemas do mundo real  
✅ Implementar pipelines completos de detecção de fraude, do zero à produção  
✅ Criar visualizações e relatórios claros para tomada de decisão

---

## 📁 Estrutura do Projeto

```
.
├── data/                  # Dados simulados
├── notebooks/             # Códigos passo a passo por etapa
├── visuals/               # Gráficos e fluxogramas
├── models/                # Modelos treinados
├── README.md              # Este arquivo
```

---

## 📫 Contato

Caso tenha interesse em conversar sobre este projeto ou discutir oportunidades:
**Daniel Victor Simões Neves**  
📧 Email: nevesdatascience@gmail.com 
💼 LinkedIn: https://www.linkedin.com/in/daniel-victor-/
