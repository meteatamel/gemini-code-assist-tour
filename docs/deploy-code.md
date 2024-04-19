# Deploy code

Next step is to deploy our code to Cloud Run with Gemini's help. You can try
different prompts but in this case, the easiest way to deploy with with
`gcloud` and source based deployment, so let's ask Gemini for that.

**Prompt**
> How can I deploy app.py to Cloud Run with gcloud source based deploy without the --image flag?

**Answer**
<blockquote>
gcloud run deploy hello-world \
--source . \
--platform managed \
--allow-unauthenticated
</blockquote>

Gemini provides a crisp command that I can tweak and deploy, nice!
