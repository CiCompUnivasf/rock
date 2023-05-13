// Lógica para adicionar mais campos de propriedade
const addButton = document.querySelector('.add-button');
const form = document.querySelector('form');
addButton.addEventListener('click', () => {
  const div = document.createElement('div');
  div.innerHTML = `
    <input type="text" name="propriedade[]" placeholder="Propriedade">
    <input type="number" name="porcentagem[]" placeholder="Porcentagem">
  `;
  form.insertBefore(div, addButton);
});