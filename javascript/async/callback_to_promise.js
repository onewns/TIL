'use strict';

// JavaScript is synchronous.
// Execute the code block in order after hoisting.
// hoisting: var, function declaration
console.log('1');
setTimeout(() => console.log('2'), 1000);
console.log('3');

// Synchronous callback
function printImmediately(print) {
  print();
}
printImmediately(() => console.log('hello'));

// Asynchronous callback
function printWithDelay(print, timeout) {
  setTimeout(print, timeout);
}
printWithDelay(() => console.log('async callback'), 2000);

// Callback Hell Example
class UserStorage {
  loginUser(id, password) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (
          (id === 'nick' && password === 'nick') ||
          (id === 'coder' && password === 'coder')
        ) {
          resolve(id);
        } else {
          reject(new Error('not found'));
        }
      }, 2000);
    });
  }

  getRoles(user) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (user === 'nick') {
          resolve({ name: 'nick', role: 'admin' });
        } else {
          reject(new Error('no access'));
        }
      }, 1000);
    })
  }
}

const userStorage = new UserStorage();
userStorage
  .loginUser('nick', 'nick')
  .then(userStorage.getRoles)
  .then(user => console.log(user))
  .catch(console.error);