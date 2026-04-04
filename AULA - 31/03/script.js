
        async function treinarEPrever() {

            // Pegando elementos da tela
            const textoStatus = document.getElementById("status");
            const textoResultado = document.getElementById("resultado");

            // Pegando valor digitado pelo usuário
            const inputMinutos = document.getElementById("minutos").value;
            const minutosDigitados = parseFloat(inputMinutos);

            // Validação de entrada
            if (!inputMinutos || isNaN(minutosDigitados) || minutosDigitados < 0) {
                textoResultado.innerText = "❌ Erro: Digite um valor válido!";
                textoStatus.innerText = "Status: Entrada inválida";
                return;
            }

            textoStatus.innerText = "Status: Treinando a IA...";

            // =========================
            // 1. CRIAR O MODELO (neurônio)
            // =========================
            const modelo = tf.sequential();
            modelo.add(tf.layers.dense({
                units: 1,
                inputShape: [1]
            }));

            // =========================
            // 2. COMPILAR O MODELO
            // =========================
            modelo.compile({
                loss: 'meanSquaredError',
                optimizer: 'sgd'
            });

            // =========================
            // 3. DADOS DE TREINO
            // X = minutos de exercício
            // Y = calorias queimadas
            // =========================
            const dadosEntrada = tf.tensor2d([10, 20, 30, 45], [4, 1]);
            const dadosSaida = tf.tensor2d([80, 160, 240, 360], [4, 1]);

            // =========================
            // 4. TREINAMENTO
            // A IA aprende com os dados
            // =========================
            await modelo.fit(dadosEntrada, dadosSaida, {
                epochs: 200
            });

            textoStatus.innerText = "Status: IA treinada!";

            // =========================
            // 5. PREVISÃO
            // =========================
            const inputTensor = tf.tensor2d([minutosDigitados], [1, 1]);
            const previsao = modelo.predict(inputTensor);

            // Convertendo resultado para número
            const valorPrevisto = previsao.dataSync()[0];

            // Mostrando resultado na tela
            textoResultado.innerText =
                "Calorias Queimadas: " + valorPrevisto.toFixed(2) + " cal";

            // Limpando memória (dispose dos tensors)
            dadosEntrada.dispose();
            dadosSaida.dispose();
            inputTensor.dispose();
            previsao.dispose();
            modelo.dispose();
        }
    