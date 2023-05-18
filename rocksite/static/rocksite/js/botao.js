// Lógica para adicionar mais campos de propriedade

var fieldsCounter = 1;

const addButton = document.querySelector('.add-button');
const form = document.querySelector('form');

function addFields() {
  const div = document.createElement('div');
  div.innerHTML = `
    <input type="text" id="propriedade${fieldsCounter}" placeholder="Propriedade">
    <input type="text" id="porcentagem${fieldsCounter}" placeholder="Porcentagem">
  `;
  form.insertBefore(div, addButton);
  fieldsCounter += 1;
}