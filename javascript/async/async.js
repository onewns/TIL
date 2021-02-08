// async & await
// clear style of using promise

// 1. async
async function fetchUser() {
  // do network request in 10 secs....
  return 'nick';
}

const user = fetchUser();
user.then(console.log);
console.log(user);

// 2. await
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function getApple() {
  await delay(200);
  return 'apple';
}

async function getBanana() {
  await delay(1000);
  return 'banana';
}

// 1초씩 2번 기다려야 함
// async function pickFruits() {
//   const apple = await getApple();
//   const banana = await getBanana();
//   return `${apple} + ${banana}`;
// }


// 요청을 시작하자 마자 보내서 1초만 기다리면 됨
// but 매우 보기 불편 => 병렬처리의 경우 밑의 promise.all 을 사용
async function pickFruits() {
  const applePromise = getApple();
  const bananaPromise = getBanana();
  const apple = await applePromise;
  const banana = await bananaPromise;
  return `${apple} + ${banana}`;
}

pickFruits().then(console.log)


// 3. useful Promise APIs
function pickAllFruits() {
  return Promise.all([getApple(), getBanana()]).then(fruits => fruits.join(' + '));
}
pickAllFruits().then(console.log);

// 빨리 응답 오는것만
function pickOnlyOne() {
  return Promise.race([getApple(), getBanana()]);
}
pickOnlyOne().then(console.log);