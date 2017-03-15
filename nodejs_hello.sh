#!/bin/bash

# update apt & install nodejs
sudo apt-get update -qq
sudo apt-get install -y npm nodejs-legacy

# install forever from npm
sudo npm install -g forever

# create script
cat << EOF > ~/node.js
var http = require('http');
var server = http.createServer(function (request, response) {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("Hello World\n");
});
server.listen(3000);
EOF

# start node.js app
forever start ~/node.js

# redirect 80 (http) to port 3000 (nodejs)
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3000

exit 0
