
function submitForm(event) {
  event.preventDefault();
  const form = document.querySelector('form');
  const propriedades = [];
  const porcentagens = [];

  for (let i = 0; i < fieldsCounter; i++) {
    const propriedade = document.getElementById(`propriedade${i}`).value;
    const porcentagem = parseFloat(document.getElementById(`porcentagem${i}`).value.replaceAll(",", "."));
    if (propriedade && porcentagem) {
      propriedades.push(propriedade);
      porcentagens.push(porcentagem);
    }
  }

  const searchParams = new URLSearchParams();
  for (let i = 0; i < propriedades.length; i++) {
    searchParams.append('propriedade[]', propriedades[i]);
    searchParams.append('porcentagem[]', porcentagens[i]);
  }
  const payload = { propriedades: propriedades, porcentagens: porcentagens }
  console.log(payload)
  console.log(`Será buscado as seguintes propriedades: ${propriedades}`)
  console.log(`Será buscado os seguintes valores: ${porcentagens}`)
  // TODO: Corrigir esse código para realizar requisição POST com propiedades e porcentagens sendo enviadas via JSON
  const url = '/search';
  const option = { method: 'POST', body: JSON.stringify(payload) }
  fetch(url, option)
    .then(response => response.json())
    .then(data => {
      console.log(data)
      //    // Manipular os dados retornados e preencher a tabela
      //    // de acordo com os resultados da busca
      // Obtém a referência ao corpo da tabela
      var tbody = document.getElementById("tables_localizacao");

      // Percorre o JSON e cria as linhas da tabela
      data.forEach(function (obj) {
        // Cria uma nova linha na tabela
        let row = document.createElement("tr");

        let descricaoCell = document.createElement("td");
        descricaoCell.textContent = obj.descricao;

        // Cria as células para o município e a UF
        let municipioCell = document.createElement("td");
        municipioCell.textContent = obj.municipio;

        let ufCell = document.createElement("td");
        ufCell.textContent = obj.uf;

        // Adiciona as células à linha
        row.appendChild(descricaoCell);
        row.appendChild(municipioCell);
        row.appendChild(ufCell);

        // Adiciona a linha ao corpo da tabela
        tbody.appendChild(row);
      });

    })
    .catch(error => {
      console.error('Ocorreu um erro na busca:', error);
    });
}

