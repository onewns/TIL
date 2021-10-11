export default ($taget, state) => {
  const todoFilter = document.createElement('div');
  todoFilter.dataset.component = 'todoFilter';

  todoFilter.innerHTML = `<button>All</button><button>Completed</button><button>Active</button>`;
  return todoFilter
}