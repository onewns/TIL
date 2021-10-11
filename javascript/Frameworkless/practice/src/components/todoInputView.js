export default ($target, state, { addItem }) => {
  const searchBar = document.createElement('div');
  searchBar.dataset.component = 'todoInput';
  
  searchBar.innerHTML = `<input>`

  const $input = searchBar.querySelector('input');
  $input.addEventListener('keypress', (e) => {if (e.key === 'Enter') {addItem(e.target.value); e.target.value = ''}})
  return searchBar
}