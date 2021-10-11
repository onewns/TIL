const http = require('http'); // 서버 실행을 위해
const https = require('https'); // 외부 api 요청을 위해


http.createServer((request, response) => {
  const { headers, method, url } = request;
  console.log(Object.keys(request));
  let body = []; 

  if (url === '/news') { // 라우팅
    console.log(headers, method, url)
    const options = {
      host: 'openapi.naver.com',
      method: 'GET',
      headers: {'X-Naver-Client-Id':'vRNqXlfqcbZPoZ0uZgpI', 'X-Naver-Client-Secret': '83jcRqbfA6', 'Content-Type': 'application/json'}
    };

    const req = https.request(`https://openapi.naver.com/v1/search/news.json?query=${encodeURI('머스크')}`, options, (res) => {
      console.log(`STATUS: ${res.statusCode}`);
      res.setEncoding('utf8');
      res.on('data', (chunk) => {
        body.push(JSON.parse(chunk))
      });
      res.on('end', () => {
        response.writeHead(200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'})
        const responseBody = { headers, method, url, body };
        response.end(JSON.stringify(responseBody));
      });
    });
    req.on('error', (e) => {
      console.error(`problem with request: ${e.message}`);
    });

    // Write data to request body
    req.end();

    
  }
  else {

    request.on('error', (err) => {
      console.error(err);
    }).on('data', (chunk) => {
      body.push(chunk);
    }).on('end', () => {
      body = Buffer.concat(body).toString();
      
      response.on('error', (err) => {
        console.error(err);
      });
      
      response.statusCode = 200;
      response.setHeader('Content-Type', 'application/json');
      const responseBody = { headers, method, url, body };
      
      response.end(JSON.stringify(responseBody));
    });
  }
}).listen(8080);

// import * as http from 'http';
// var http = require('http')

// http.get('http://localhost:8000/', (res) => {
//   const { statusCode } = res;
//   const contentType = res.headers['content-type'];
//   console.log(res)

//   let error;
//   // Any 2xx status code signals a successful response but
//   // here we're only checking for 200.
//   if (statusCode !== 200) {
//     error = new Error('Request Failed.\n' +
//                       `Status Code: ${statusCode}`);
//   } else if (!/^application\/json/.test(contentType)) {
//     error = new Error('Invalid content-type.\n' +
//                       `Expected application/json but received ${contentType}`);
//   }
//   if (error) {
//     console.error(error.message);
//     // Consume response data to free up memory
//     res.resume();
//     return;
//   }

//   res.setEncoding('utf8');
//   let rawData = '';
//   res.on('data', (chunk) => { rawData += chunk; });
//   res.on('end', () => {
//     try {
//       const parsedData = JSON.parse(rawData);
//       console.log(parsedData);
//     } catch (e) {
//       console.error(e.message);
//     }
//   });
// }).on('error', (e) => {
//   console.error(`Got error: ${e.message}`);
// });

// // Create a local server to receive data from
// const server = http.createServer((req, res) => {
//   res.writeHead(200, { 'Content-Type': 'application/json' });
//   res.end(JSON.stringify({
//     data: 'Hello World!'
//   }));
// });

// server.listen(8000);


// var https = require('https');
// var options = {
//     // host: 'openapi.naver.com',
//     // path: `/search/news.json?query=${encodeURI('머스크')}`,
//     headers: {'X-Naver-Client-Id':'vRNqXlfqcbZPoZ0uZgpI', 'X-Naver-Client-Secret': '83jcRqbfA6'}
//   };
 
// function handleResponse(response) {
//   var serverData = '';
//   console.log(response.on)
//   response.on('data', function (chunk) {
//     serverData += chunk;
//   });
//   response.on('end', function () {
//     console.log("received server data:");
//     // console.log(serverData);
//   });
// }
 
// var serverData = '';
// https.get(`https://openapi.naver.com/v1/search/news.json?query=${encodeURI('에스파')}`, options, function(response){
//   response.on('data', function (chunk) {
//     serverData += chunk;
//   });
//   response.on('end', function () {
//     console.log("received server data:");
//     console.log(serverData);
//   });
// });

// var http = require('http');
 
// var server = http.createServer();
 
// var host = 'localhost';
// var port = 3000;
// server.listen(port, host, 50000, function(){
//     console.log('웹서버 실행됨.');
// });
 
// server.on('connection', function(socket){
//     console.log('클라이언트가 접속했습니다.');
// });
 
// server.on('request', function(req,res){
//     console.log('클라이언트 요청이 들어왔습니다.');
//     // console.dir(req);
    
//     res.writeHead(200, {"Content-Type":"application/json"});
//     res.write(JSON.stringify({1: serverData}));
//     res.end();
// });
 
// const https = require('https')

// const postData = JSON.stringify({
//   'msg': 'Hello World!'
// });

// const options = {
//   host: 'openapi.naver.com',
//   // port: 80,
//   // path: '/upload',
//   method: 'GET',
//   headers: {'X-Naver-Client-Id':'vRNqXlfqcbZPoZ0uZgpI', 'X-Naver-Client-Secret': '83jcRqbfA6'}
// };

// const req = https.request(`https://openapi.naver.com/v1/search/news.json?query=${encodeURI('에스파')}`, options, (res) => {
//   console.log(`STATUS: ${res.statusCode}`);
//   // console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
//   res.setEncoding('utf8');
//   res.on('data', (chunk) => {
//     // console.log(`BODY: ${chunk}`);
//   });
//   res.on('end', () => {
//     console.log('No more data in response.');
//   });
// });

// req.on('error', (e) => {
//   console.error(`problem with request: ${e.message}`);
// });

// // Write data to request body
// req.write(postData);
// req.end(postData);




// app.get('/search/blog', function (req, res) {
//   var api_url = 'https://openapi.naver.com/v1/search/blog?query=' + encodeURI(req.query.query); // json 결과
// //   var api_url = 'https://openapi.naver.com/v1/search/blog.xml?query=' + encodeURI(req.query.query); // xml 결과
//   var request = require('request');
//   var options = {
//       url: api_url,
//       headers: {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret': client_secret}
//    };
//   request.get(options, function (error, response, body) {
//     if (!error && response.statusCode == 200) {
//       res.writeHead(200, {'Content-Type': 'text/json;charset=utf-8'});
//       res.end(body);
//     } else {
//       res.status(response.statusCode).end();
//       console.log('error = ' + response.statusCode);
//     }
//   });
// });
// app.listen(3000, function () {
//   console.log('http://127.0.0.1:3000/search/blog?query=검색어 app listening on port 3000!');
// });

