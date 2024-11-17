document.getElementById("searchForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const query = document.getElementById("searchInput").value;
    const resultContainer = document.getElementById("result");

    try {
        const response = await fetch("http://127.0.0.1:8000/pesquisar", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `pesquisa=${encodeURIComponent(query)}`
        });

        if (!response.ok) {
            throw new Error("Erro ao buscar dados.");
        }

        const data = await response.json();
        console.log(data);  // Verifique o conteúdo da resposta

        // Limpa o container de resultados e exibe os novos
        resultContainer.innerHTML = "<h2>Resultados:</h2>";

        if (Array.isArray(data.sentimentos)) {
            data.sentimentos.forEach((item, index) => {
                const commentElement = document.createElement("div");
                commentElement.classList.add("comment-box"); // Adiciona a classe de estilo

                commentElement.innerHTML = `
                    <p><strong>Comentário ${index + 1}:</strong> ${item.text}</p>
                    <p><strong>Sentimento:</strong> ${item.sentiment}</p>
                    <p><strong>Confiança:</strong> ${item.confidence}</p>
                `;
                resultContainer.appendChild(commentElement);
            });
        } else {
            resultContainer.innerHTML = `<p style="color: red;">Formato de resposta inválido.</p>`;
        }
    } catch (error) {
        resultContainer.innerHTML = `<p style="color: red;">${error.message}</p>`;
    }
});
