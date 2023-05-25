
function submitForm(event) {
  event.preventDefault();
  const form = document.querySelector('form');
  const payload = {};


  for (let i = 0; i < fieldsCounter; i++) {
    const propriedade = document.getElementById(`propriedade${i}`).value;
    const porcentagem = parseFloat(document.getElementById(`porcentagem${i}`).value.replaceAll(",", "."));
    if (propriedade && porcentagem) {
     payload[propriedade] = porcentagem;
    }
  }

 
  console.log(payload)
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
      tbody.innerHTML = " ";

      // Percorre o JSON e cria as linhas da tabela
      data.forEach(function (obj) {
        // Cria uma nova linha na tabela
        let row = document.createElement("tr");

        // Cria as células para o município e a UF
        let municipioCell = document.createElement("td");
        municipioCell.textContent = obj.municipio;

        
        let ufCell = document.createElement("td");
        ufCell.textContent = obj.uf;

        let usoAtualCell = document.createElement("td");
        usoAtualCell.textContent = obj.uso_atual;

        let descricaoCell = document.createElement("td");
        descricaoCell.textContent = obj.descricao;


        // Adiciona as células à linha
        row.appendChild(municipioCell);
        row.appendChild(ufCell);
        row.appendChild(usoAtualCell);
        row.appendChild(descricaoCell);

        // Adiciona a linha ao corpo da tabela
        tbody.appendChild(row);
      });

    })
    .catch(error => {
      console.error('Ocorreu um erro na busca:', error);
    });
}

