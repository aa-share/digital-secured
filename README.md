# Digital Secured

A lightweight static gateway designed to protect online documents (such as a CV or resume) from automated web scraping using **Cloudflare Turnstile** and high-entropy filename obfuscation.

[Live Demo](https://aa-share.github.io/digital-secured/)

---

## Features

* **Bot Protection:** Requires Cloudflare Turnstile verification before embedding the target document.
* **Obfuscated Paths:** Stores documents under randomized UUID filenames to prevent direct URL guessing.
* **Crawler Blocking:** Pre-configured `robots.txt` disallows indexing of the static asset directory.
* **Mobile & Dark Mode Optimized:** Uses `<object>` embedding with automatic system theme adaptation.

---

## Document Generation

To generate a new obfuscated filename for your PDF document, run:

```bash
python3 -c 'import uuid; print(f"doc_{uuid.uuid4().hex}.pdf")'
```

## Tests
```bash
python3 -m unittest test_site.py -v
python3 -m http.server 8000
```
[Localhost access](http://localhost:8000/index.dev.html)
