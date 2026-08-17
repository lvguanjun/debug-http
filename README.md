<div align="center">

# debug-http

A minimal HTTP debug service that echoes request details back with any status code you want.

**[English](README.md) | [中文](README_CN.md)**

[![Build](https://github.com/lvguanjun/debug-http/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/lvguanjun/debug-http/actions/workflows/docker-publish.yml)
[![License: MIT](https://img.shields.io/github/license/lvguanjun/debug-http)](LICENSE)
[![Docker Image](https://img.shields.io/badge/ghcr.io-debug--http-blue?logo=docker)](https://ghcr.io/lvguanjun/debug-http)

</div>

---

## Quick Start

```bash
docker run -p 8000:8000 ghcr.io/lvguanjun/debug-http:latest
```

Or run locally with [uv](https://docs.astral.sh/uv/):

```bash
uv run uvicorn debug_http.main:app --reload
```

## Usage

Send **any HTTP method** to `/status/{code}` (or `/status/{code}/any/path`), get your request echoed back with that status code. `/status/{code}` acts as a prefix — any trailing path is accepted.

```bash
curl -X POST http://localhost:8000/status/201/api/test \
  -H "Content-Type: application/json" \
  -d '{"hello": "world"}'
```

Response (HTTP 201):

```json
{
  "method": "POST",
  "path": "/status/201/api/test",
  "headers": {
    "host": "localhost:8000",
    "content-type": "application/json",
    "user-agent": "curl/8.5.0"
  },
  "query_params": {},
  "body": {"hello": "world"},
  "client_ip": "127.0.0.1"
}
```

## Features

| Feature | Description |
|---------|-------------|
| Any HTTP method | GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS |
| Custom status code | 100–599, specified in path |
| Prefix matching | `/status/{code}` matches any trailing path |
| Smart body parsing | Auto-detects JSON regardless of Content-Type |
| Full echo | Path, headers, query params, body, client IP |

## Deployment

### Docker Compose

```yaml
services:
  debug-http:
    image: ghcr.io/lvguanjun/debug-http:latest
    ports:
      - "8000:8000"
    restart: unless-stopped
```

### CI/CD

Push to `main` → builds `latest` image. Push a `v*` tag → builds versioned image.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=lvguanjun/debug-http&type=Date)](https://star-history.com/#lvguanjun/debug-http&Date)

## License

[MIT](LICENSE)
