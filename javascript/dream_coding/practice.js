new Promise(function (resolve, reject) {
  setTimeout(function () {
    var name = '에스프레소';
    console.log(nama, resolve);
    resolve(name);
    console.log(resolve(name))
  }, 5000)
}).then(function (prevName) {
  console.log(prevName)
})