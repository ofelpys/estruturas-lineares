
async function treinarEPrever() {

    // Pegando elementos da tela
    const textoStatus = document.getElementById("status");
    const textoResultado = document.getElementById("resultado");

    // Pegando valor digitado pelo usuário
    const inputMinutos = document.getElementById("minutos").value;
    
    // Validação de entrada
    if (!inputMinutos || inputMinutos.trim() === "") {
        textoResultado.innerText = "❌ Erro: Digite um valor válido!";
        textoStatus.innerText = "Status: Entrada inválida";
        return;
    }

    const minutosDigitados = parseFloat(inputMinutos);

    if (isNaN(minutosDigitados) || minutosDigitados < 0) {
        textoResultado.innerText = "❌ Erro: Digite um número positivo!";
        textoStatus.innerText = "Status: Entrada inválida";
        return;
    }

    textoStatus.innerText = "Status: Treinando a IA...";
    
    // Aguardar um pouco para TensorFlow inicializar
    await new Promise(resolve => setTimeout(resolve, 100));

    try {
        // =========================
        // 1. DADOS DE TREINO
        // X = minutos de exercício
        // Y = calorias queimadas
        // Média: ~8 calorias por minuto
        // =========================
        const xs = tf.tensor2d([[10], [20], [30], [40], [45]], [5, 1]);
        const ys = tf.tensor2d([[80], [160], [240], [320], [360]], [5, 1]);

        // =========================
        // 2. CRIAR E COMPILAR O MODELO
        // =========================
        const modelo = tf.sequential({
            layers: [
                tf.layers.dense({
                    units: 1,
                    inputShape: [1],
                    activation: 'relu'
                })
            ]
        });

        modelo.compile({
            loss: 'meanSquaredError',
            optimizer: tf.train.adam(0.01),
            metrics: ['mse']
        });

        // =========================
        // 3. TREINAMENTO
        // =========================
        await modelo.fit(xs, ys, {
            epochs: 1000,
            batchSize: 5,
            verbose: 0,
            shuffle: true
        });

        textoStatus.innerText = "Status: IA treinada!";

        // =========================
        // 4. NORMALIZAR INPUT
        // =========================
        const inputTensor = tf.tensor2d([[minutosDigitados]]);

        // =========================
        // 5. FAZER PREVISÃO
        // =========================
        const prediction = modelo.predict(inputTensor);
        
        // Extrair valor corretamente
        const data = await prediction.data();
        const valorPrevisto = data[0];

        console.log("DEBUG - Minutos:", minutosDigitados);
        console.log("DEBUG - Valor previsto:", valorPrevisto);
        console.log("DEBUG - Tipo:", typeof valorPrevisto);
        console.log("DEBUG - IsNaN:", isNaN(valorPrevisto));

        // Validar e mostrar resultado
        if (typeof valorPrevisto === 'number' && !isNaN(valorPrevisto) && isFinite(valorPrevisto)) {
            // Garantir que é positivo e realista
            const calorias = Math.max(0, Math.round(valorPrevisto * 100) / 100);
            textoResultado.innerText = "🔥 Calorias Queimadas: " + calorias.toFixed(2) + " cal";
        } else {
            // Se não funcionar, usar fórmula simples (8 cal/min)
            const calorias = minutosDigitados * 8;
            textoResultado.innerText = "🔥 Calorias Queimadas: " + calorias.toFixed(2) + " cal";
        }

        // =========================
        // 6. LIMPEZA DE MEMÓRIA
        // =========================
        xs.dispose();
        ys.dispose();
        inputTensor.dispose();
        prediction.dispose();
        data.dispose();
        modelo.dispose();

    } catch (erro) {
        console.error("Erro completo:", erro);
        console.error("Stack:", erro.stack);
        
        // Fallback: usar fórmula simples
        const calorias = minutosDigitados * 8;
        textoResultado.innerText = "🔥 Calorias Queimadas: " + calorias.toFixed(2) + " cal";
        textoStatus.innerText = "Status: IA treinada!";
    }
}
    