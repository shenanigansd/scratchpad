"""Check for new tickets with DSTs available, download the DSTs, and close the ticket."""

import json
import re
from pathlib import Path

import httpx
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    """Our default configuration for models that should load from .env files."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )


class _Zendesk(EnvConfig, env_prefix="zendesk_"):
    """UPS auth."""

    base_url: str = ""
    username: str = ""
    api_token: str = ""


Zendesk = _Zendesk()


def search(client: httpx.Client) -> list[int]:
    """Find open tickets titled "need dst" with attachments and return the ticket numbers."""
    params = {
        "query": "need dst status:open status:pending status:new order_by:updated_at sort:desc has_attachment:true",
    }
    response = client.get("/api/v2/search.json", params=params)

    tickets_with_dsts_available = []
    for ticket in response.json()["results"]:
        subject_pieces = ticket["subject"].lower().replace(",", "").split(" ")
        for piece in subject_pieces:
            if re.match(r"d[\w\d]{5}", piece):
                tickets_with_dsts_available.append(ticket["id"])  # noqa: PERF401 -- false positive, not possible
    return tickets_with_dsts_available


def download_dsts(client: httpx.Client, ticket_number: int) -> None:
    response = client.get(f"/api/v2/tickets/{ticket_number}/comments.json")
    comments = response.json()
    for comment in comments["comments"]:
        for attachment in comment["attachments"]:
            # see if this matches the base URL
            attachment_bytes = client.get(attachment["content_url"], auth=client.auth).content
            Path(attachment["file_name"]).write_bytes(attachment_bytes)


def comment_and_close(client: httpx.Client, ticket_number: int) -> None:
    data = {
        "ticket": {
            "status": "solved",
            "comment": {
                "body": "Automatically processed",
                "author_id": 380031530892,
                "public": False,
            },
        },
    }
    client.put(f"/api/v2/tickets/{ticket_number}.json", data=json.dumps(data))


def run() -> None:
    auth = httpx.BasicAuth(username=Zendesk.username, password=Zendesk.api_token)
    client = httpx.Client(base_url=Zendesk.base_url, auth=auth, headers={"Content-Type": "application/json"})

    for ticket_number in search(client):
        download_dsts(ticket_number)
        # comment_and_close(ticket_number)


if __name__ == "__main__":
    run()
