
function submitForm(event) {
  event.preventDefault();
  const form = document.querySelector('form');
  const propriedades = [];
  const porcentagens = [];

  for (let i = 0; i < fieldsCounter; i++) {
    const propriedade = document.getElementById(`propriedade${i}`).value;
    const porcentagem = document.getElementById(`porcentagem${i}`).value;
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

  console.log(`Será buscado as seguintes propriedades: ${propriedades}`)
  console.log(`Será buscado os seguintes valores: ${porcentagens}`)
  // TODO: Corrigir esse código para realizar requisição POST com propiedades e porcentagens sendo enviadas via JSON
  //const url = 'processar_busca.php?' + searchParams.toString();
  //fetch(url)
  //  .then(response => response.json())
  //  .then(data => {
  //    // Manipular os dados retornados e preencher a tabela
  //    // de acordo com os resultados da busca
  //  })
  //  .catch(error => {
  //    console.error('Ocorreu um erro na busca:', error);
  //  });
}

