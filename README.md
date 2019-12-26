certbot DNS webservice
======================

Example call

```
certbot certonly -d mydomain.com \
    -a certbot-dns-webservice:dns-webservice \
    --certbot-dns-webservice:dns-webservice-url https://mywebservice.com/ \
    --certbot-dns-webservice:dns-webservice-credentials username:password
```

Of course, replace `mydomain.com` with the domain(s) you want to obtain the certificate for, `https://mywebservice.com/` with the update endpoint of your webservice and `username:password` with the respective basic auth credentials.
