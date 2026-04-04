# 🔥 Previsão de Calorias - Machine Learning com TensorFlow.js

## 📋 Resumo do Projeto

Este projeto implementa uma **rede neural simples** usando **TensorFlow.js** para prever a quantidade de **calorias queimadas** com base no **tempo de exercício em minutos**.

---

## 🔄 Alterações Realizadas

### 📝 **index.html**

#### Melhorias Estruturais:
- ✅ Adicionado `<meta charset="UTF-8">` e `<meta viewport>` para compatibilidade mobile
- ✅ Vinculação do arquivo CSS externo (`style.css`)
- ✅ Estrutura semântica com classes de estilo vaporwave

#### Mudanças de Tema:

| Elemento | Antes | Depois |
|----------|-------|--------|
| **Título** | `⚡ PREVISÃO DE NOTAS ⚡` | `🔥 QUEIMADOR DE CALORIAS 🔥` |
| **Label do Input** | "Horas de Estudo" | "Minutos de Exercício" |
| **ID do Input** | `id="horas"` | `id="minutos"` |
| **Atributos Input** | `min="0" step="0.5"` | `min="0" step="1"` |
| **Placeholder** | "Ex: 5" | "Ex: 30" |
| **Texto Botão** | "Treinar e Prever" | "Treinar IA & Prever" |

#### Estilização:
- ✅ Classe `.input` para inputs com tema ciano/néon
- ✅ Classe `.button` com gradiente magenta-ciano e efeitos hover
- ✅ Classes `.label` e `.form-group` para validação visual
- ✅ Elementos `status` e `resultado` com cores temáticas (ciano e magenta)

---

### 🤖 **script.js**

#### Mudanças Funcionais:

**1. Entrada do Usuário:**
```javascript
// ANTES
const horasDigitadas = Number(document.getElementById("horas").value);

// DEPOIS
const minutosDigitados = Number(document.getElementById("minutos").value);
```

**2. Dados de Treino:**
```javascript
// ANTES (Horas de estudo → Notas)
const dadosEntrada = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const dadosSaida = tf.tensor2d([2, 4, 6, 8], [4, 1]);

// DEPOIS (Minutos de exercício → Calorias queimadas)
const dadosEntrada = tf.tensor2d([10, 20, 30, 45], [4, 1]);
const dadosSaida = tf.tensor2d([80, 160, 240, 360], [4, 1]);
```

**Padrão de Dados:**
- 10 min → 80 cal
- 20 min → 160 cal
- 30 min → 240 cal
- 45 min → 360 cal
- **Taxa:** ~8 calorias por minuto

**3. Previsão e Output:**
```javascript
// ANTES
textoResultado.innerText = "Nota Prevista: " + valorPrevisto.toFixed(2);

// DEPOIS
textoResultado.innerText = "Calorias Queimadas: " + valorPrevisto.toFixed(2) + " cal";
```

---

## 🏗️ Estrutura do Modelo TensorFlow.js

A **arquitetura neural permaneceu intacta**:

```
┌─────────────────────────────────────┐
│  1. CRIAR MODELO SEQUENCIAL         │
│     └─ Dense Layer (1 neurônio)     │
├─────────────────────────────────────┤
│  2. COMPILAR MODELO                 │
│     └─ Loss: meanSquaredError       │
│     └─ Optimizer: SGD               │
├─────────────────────────────────────┤
│  3. DADOS DE TREINO (4 amostras)    │
│     └─ Input: minutos de exercício  │
│     └─ Output: calorias queimadas   │
├─────────────────────────────────────┤
│  4. TREINAMENTO (200 épocas)        │
│     └─ Aprende relação linear       │
├─────────────────────────────────────┤
│  5. PREVISÃO                        │
│     └─ Entrada: minutos do usuário  │
│     └─ Saída: calorias estimadas    │
└─────────────────────────────────────┘
```

---

## 🎨 Tema Visual (Vaporwave)

- **Paleta de Cores:**
  - 🟣 Magenta (`#ff00ff`) - Títulos e destaques
  - 🔵 Ciano (`#00ffff`) - Labels e inputs
  - 🟡 Fundo gradiente - Roxo escuro (`#0f0c29` → `#302b63`)

- **Efeitos:**
  - ✨ Brilho de entrada (shimmer animation)
  - 🌟 Glow text nos títulos
  - 🎯 Hover effects nos botões e inputs
  - 📐 Padrão geométrico de fundo animado

---

## 💡 Como Usar

1. **Abrir no navegador:** Abra o arquivo `index.html` em um navegador moderno
2. **Inserir minutos:** Digite a quantidade de minutos de exercício (ex: 30)
3. **Clicar em "Treinar IA & Prever":** A IA vai treinar e fazer a previsão
4. **Ver resultado:** As calorias queimadas estimadas aparecerão em magenta

---

## 📊 Exemplo de Execução

**Entrada:** 25 minutos
**Saída esperada:** ~200 calorias (aproximadamente 8 cal/min)
**Status:** "Status: IA treinada!"

---

## 🔧 Tecnologias Utilizadas

- **HTML5** - Estrutura semântica
- **CSS3** - Tema vaporwave com animações
- **JavaScript (ES6+)** - Lógica de previsão
- **TensorFlow.js** - Rede neural via CDN

---

## 📦 Arquivos do Projeto

```
├── index.html      ← Interface com tema calorias
├── script.js       ← Modelo de IA com dados adaptados
├── style.css       ← Tema vaporwave
└── README.md       ← Este arquivo
```

---

**Desenvolvido em:** 3 de abril de 2026  
**Tema:** Previsão de Calorias por Minuto de Exercício 🏋️‍♂️⚡
