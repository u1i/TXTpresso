![](txtpresso-small.png)

# TXTpresso

TXTpresso is an unconventional and experimental project aimed at exploring the possibilities of using DNS protocol and TXT records with zero-second TTL for lightweight API-like data communication. Welcome to the geeky side of internet protocols!


# Example

### Usage

`dig @127.0.0.1 time.txtpresso TXT +short`

`"2024-02-01 13:44:35"`

### Code

[![](https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/TXTpresso/)

```
from txtpresso.server import TXTpressoServer, BaseHandler
from datetime import datetime

class TimeHandler(BaseHandler):
    def handle(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    server = TXTpressoServer()
    server.register_handler('time', TimeHandler)
    server.start()
```

## Goal

The goal of TXTpresso is to use the DNS protocol's unique features to create a lightweight, fast, and potentially harder-to-detect communication system compared to traditional HTTP APIs.

## Concept

Using DNS TXT records and UDP, TXTpresso offers simple and swift communication methods compared to the overhead of HTTP requests, headers, and JSON payloads. By using unique lookups, such as test${UTIME}.domain, TXTpresso bypasses some caching issues, though users should be cautious of the potential impact on DNS traffic and server load.

## Use Cases

1. Bypassing firewalls or restrictions: By using DNS instead of HTTP APIs, this "under-the-radar" method might allow for communication in scenarios where traditional internet access is limited or blocked.
2. Lightweight communication: If the emphasis is on simplicity and speed rather than robustness, using DNS lookups and UDP might keep things fast and lightweight compared to a full-blown HTTP API.
3. Novel applications or hacks: As a fun, experimental project, you could come up with neat applications that take advantage of the DNS protocol's unique characteristics.

## Methods

### GET

TXTpresso's GET method is is using the concept of utilizing subdomains to represent queries or endpoints. By sending a DNS query for a TXT record on a specific subdomain (like `time.domain`), you essentially request data associated with that subdomain. The server, in turn, processes the query and sends back the corresponding data in the TXT record.

Example: To query the current time, use the `dig` command to search for a TXT record on `time.domain`:

```
dig @txtpresso.server.com +short txt time.txtpresso
```

### POST

TXTpresso's POST method relies on BASE64-encoding the data you want to send and embedding it as part of a subdomain in a DNS query. This approach essentially transforms the subdomain into a carrier of your data payload. Upon receiving the query, the server decodes the information from the subdomain and processes it accordingly.

Example: Encode your data (limited to 512 bytes) in a DNS-friendly format, such as Base64, and send it as a subdomain for a DNS query.

```
dig @txtpresso.server.com +short a c3VwZXJ0cm91cGVyCg.post.txtpresso
```

## Caveats

Be mindful of some limitations when using TXTpresso:

1. Increased DNS traffic and potential server load.
2. Caching complications, depending on unique lookups.
3. Limitations in data size - a maximum of 512 bytes.
4. Potential latency and packet loss with UDP.

## Reminder

This experimental project is intended for educational purposes and to demonstrate the unconventional application of the DNS protocol. Always consider the broader impact on internet infrastructure and use TXTpresso responsibly.
