1. Copy the manifest to `~/Library/Containers/com.microsoft.Word/Data/Documents/wef` or `~/Library/Containers/com.microsoft.Powerpoint/Data/Documents`
1. Add-ins need to be served over HTTPS. Run [`caddy`](https://caddyserver.com) to use the local `Caddyfile` config. It starts a local file server on [`https://localhost:2020`](https://localhost:2020/home.html).
1. Since the certificate is self-signed, you’ll need to trust it initially
1. In Word or PowerPoint, Insert > My Add-ins and make sure to use the drop-down arrow *not* the button