export default ($target, state, events) => {
  const header = document.createElement('div');
  header.dataset.component = 'header'
  header.innerHTML = `<h1>TODO!</h1>`
  return header
}