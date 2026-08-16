<div align="center">

# debug-http

轻量 HTTP 调试服务 —— 将请求原样回显，帮你排查客户端到底发了什么。

**[English](README.md) | [中文](README_CN.md)**

[![Build](https://github.com/lvguanjun/debug_http/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/lvguanjun/debug_http/actions/workflows/docker-publish.yml)
[![License: MIT](https://img.shields.io/github/license/lvguanjun/debug_http)](LICENSE)
[![Docker Image](https://img.shields.io/badge/ghcr.io-debug__http-blue?logo=docker)](https://ghcr.io/lvguanjun/debug_http)

</div>

---

## 快速开始

```bash
docker run -p 8000:8000 ghcr.io/lvguanjun/debug_http:latest
```

或使用 [uv](https://docs.astral.sh/uv/) 本地运行：

```bash
uv run uvicorn main:app --reload
```

## 使用方法

向 `/status/{code}` 发送**任意 HTTP 方法**，服务以指定状态码响应，并回显请求详情。

```bash
curl -X POST http://localhost:8000/status/201 \
  -H "Content-Type: application/json" \
  -d '{"hello": "world"}'
```

响应（HTTP 201）：

```json
{
  "method": "POST",
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

## 功能特性

| 特性 | 说明 |
|------|------|
| 任意 HTTP 方法 | GET、POST、PUT、PATCH、DELETE、HEAD、OPTIONS |
| 自定义状态码 | 100–599，通过路径参数指定 |
| 智能 body 解析 | 自动尝试 JSON 反序列化，不依赖 Content-Type |
| 完整回显 | 请求头、查询参数、请求体、客户端 IP |

## 部署

### Docker Compose

```yaml
services:
  debug-http:
    image: ghcr.io/lvguanjun/debug_http:latest
    ports:
      - "8000:8000"
    restart: unless-stopped
```

### CI/CD

推送 `main` 分支 → 构建 `latest` 镜像。推送 `v*` tag → 构建版本号镜像。

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=lvguanjun/debug_http&type=Date)](https://star-history.com/#lvguanjun/debug_http&Date)

## 许可证

[MIT](LICENSE)
