# Ask VOIZON AI backend

This Worker keeps the OpenAI API key on the server. Never put the key in website JavaScript or commit it to GitHub.

## Deploy (Cloudflare Workers)

1. Create/sign in to a Cloudflare account and open **Workers & Pages**.
2. Create a Worker named `voizon-ask-assistant`.
3. Paste the contents of `src/index.js` into the Worker editor and deploy.
4. In the Worker settings, add a secret named `OPENAI_API_KEY` with your OpenAI API key. Do not share or commit the key.
5. Keep the variable `OPENAI_MODEL` set to `gpt-5.5` (or a model enabled for your API project).
6. Copy the Worker URL. The chat page will need this endpoint with `/chat` appended.
7. In `assets/js/ask-voizon.js`, replace `YOUR_CLOUDFLARE_WORKER_URL` with your Worker base URL, e.g. `https://voizon-ask-assistant.<your-subdomain>.workers.dev`. Commit and push that change.

The Worker only accepts requests from the published GitHub Pages origin:
`https://salmanulfariskk555-gif.github.io`

## Local deploy with Wrangler

Install Wrangler and authenticate with Cloudflare. From this folder:

```bash
npx wrangler secret put OPENAI_API_KEY
npx wrangler deploy
```

Set the secret when prompted. Do not put it in `wrangler.toml`.

## Notes

- The website sends only the visitor's current question and a short recent chat history.
- The Worker does not save conversations; OpenAI requests set `store: false`.
- Add Cloudflare rate limiting / usage alerts before promoting the chat widely.
- API usage is billed separately by OpenAI. Set a usage budget/alert in the API project.
- This assistant is for general service enquiries. It must not invent quotes, guarantees, testimonials or client details.
