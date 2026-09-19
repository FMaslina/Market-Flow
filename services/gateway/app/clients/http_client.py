from aiohttp import ClientResponse, ClientSession
from starlette.datastructures import URL


class HttpClient:
    def __init__(
        self,
        client_session: ClientSession,
        timeout: int = 20,
    ):
        self.timeout = timeout
        self.session = client_session

    async def get(
        self,
        url: str | URL,
        params: dict | list[tuple] | None = None,
        allow_redirect: bool = True,
    ) -> ClientResponse:
        response = await self.session.get(
            url=url, params=params, allow_redirects=allow_redirect, timeout=self.timeout
        )
        return response

    async def post(
        self,
        url: str | URL,
        body: dict,
        params: dict | list[tuple] | None = None,
        allow_redirect: bool = True,
    ) -> ClientResponse:
        response = await self.session.post(
            url=url,
            json=body,
            params=params,
            allow_redirects=allow_redirect,
            timeout=self.timeout,
        )
        return response

    async def put(
        self,
        url: str | URL,
        body: dict,
        params: dict | list[tuple] | None = None,
        allow_redirect: bool = True,
    ) -> ClientResponse:
        response = await self.session.put(
            url=url,
            json=body,
            params=params,
            allow_redirects=allow_redirect,
            timeout=self.timeout,
        )
        return response

    async def patch(
        self,
        url: str | URL,
        body: dict,
        params: dict | list[tuple] | None = None,
        allow_redirect: bool = True,
    ) -> ClientResponse:
        response = await self.session.patch(
            url=url,
            json=body,
            params=params,
            allow_redirects=allow_redirect,
            timeout=self.timeout,
        )
        return response

    async def delete(
        self,
        url: str | URL,
        params: dict | list[tuple] | None = None,
        allow_redirect: bool = True,
    ) -> ClientResponse:
        response = await self.session.delete(
            url=url,
            params=params,
            allow_redirects=allow_redirect,
            timeout=self.timeout,
        )
        return response
