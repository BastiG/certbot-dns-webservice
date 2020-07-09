# certbot DNS webservice
======================

An authentication plugin for certbot which allows DNS modification through a DynDNS 2 like interface. See [[1](#references)] for an example web service.

## Installation

Clone the repository to a local directory, e.g. `/opt/certbot-dns-webservice`.
```
cd /opt/certbot-dns-webservice
pip install .
```

## Usage

Example call

```
certbot certonly -d mydomain.com \
    -a certbot-dns-webservice:dns-webservice \
    --certbot-dns-webservice:dns-webservice-url https://mywebservice.com/dyn/update \
    --certbot-dns-webservice:dns-webservice-credentials username:password
```

Of course, replace `mydomain.com` with the domain(s) you want to obtain the certificate for, `https://mywebservice.com/dyn/update` with the update endpoint of your webservice and `username:password` with the respective basic auth credentials.

## References

[1] https://github.com/BastiG/dyndns-pdns