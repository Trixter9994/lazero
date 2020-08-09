const http = require('http');

http.get('http://cache.baiducontent.com/c?m=9d78d513d9d437ac4f9ae4697c65c010184381132ba1d60209a28439e5732840506793e777710705a3d20a6216dc3a4b9af02101301767f7c5c7d20c9bf985295c953a753241c60753c419d88a1d799237902db8f246f0ba8763cfb382809e0d048c035624deedd70a5309ca6df31f26e3d09a4a025f66b8e72d33a2086029e9781be710b1a7652a0584f1da5a4bc73dd01650cde96aee&amp;', (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    console.log(data);
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});
