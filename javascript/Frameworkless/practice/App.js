import headerView from './src/components/headerView.js';
import todoInputView from './src/components/todoInputView.js';
import todosView from './src/components/todosView.js';
import todoFilterView from './src/components/todoFilterView.js';


function App($target) {
  const state = {
    todos: [
      {
        title: 'react',
        completed: false
      },
      {
        title: 'vue',
        completed: false
      },
      {
        title: 'django',
        completed: false
      },
      {
        title: 'javascript',
        completed: false
      }
    ],
    option: 'all'
  }
  const header = document.createElement('div');
  $target.appendChild(header)

  const components = [
    headerView($target),
    todoInputView($target),
    todosView($target, state),
    todoFilterView($target)
  ]

  components.forEach(component => $target.appendChild(component))
}

export default App