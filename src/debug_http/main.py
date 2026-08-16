from __future__ import annotations

import json

import uvicorn
from fastapi import FastAPI, Request, Response

app = FastAPI(title="Debug HTTP", description="Echo request details for debugging")


@app.api_route("/status/{code}", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"])
async def echo(code: int, request: Request) -> Response:
    if not (100 <= code <= 599):
        return Response(
            content=json.dumps({"error": f"Invalid status code: {code}. Must be between 100 and 599."}),
            status_code=400,
            media_type="application/json",
        )

    raw_body = await request.body()
    body: str | dict | list | None = None
    if raw_body:
        try:
            body = json.loads(raw_body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            body = raw_body.decode("utf-8", errors="replace")

    payload = {
        "method": request.method,
        "headers": dict(request.headers),
        "query_params": dict(request.query_params),
        "body": body,
        "client_ip": request.client.host if request.client else None,
    }

    return Response(
        content=json.dumps(payload, ensure_ascii=False, indent=2),
        status_code=code,
        media_type="application/json",
    )


def cli() -> None:
    uvicorn.run("main:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    cli()
