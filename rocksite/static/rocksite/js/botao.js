// Lógica para adicionar mais campos de propriedade

var fieldsCounter = 1;

const addButton = document.querySelector('.add-button');
const form = document.querySelector('form');

function addFields() {
  const div = document.createElement('div');
  div.innerHTML = `
    <select id="propriedade${fieldsCounter}">
      <option value="h2o"> H2O (pH) </option>
      <option value="calcio">Cálcio (cmol/kg) </option>
      <option value="kcl">Cloreto de Potássio (pH) </option>
    </select>
    <input type="text" id="porcentagem${fieldsCounter}" placeholder="Porcentagem">
  `;
  form.insertBefore(div, addButton);
  fieldsCounter += 1;
}