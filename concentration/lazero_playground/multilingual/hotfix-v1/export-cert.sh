#!/bin/bash
server=www.baidu.com
port=443
echo | openssl s_client -connect $server:$port 2>&1 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > baidu.cert.pem
