# Run application locally

It's time to run the application locally. Let's see what kind of help we can get
from Gemini.

**Prompt**
> How can I run app.py with flask command?

**Answer**
<blockquote>

To run the `app.py` script using the Flask command, you can use the following steps:

1. Ensure that you have Python and Flask installed on your system.
1. Navigate to the directory where your `app.py` script is located.
1. Open a terminal or command prompt.
1. Run the following command: `flask run`

</blockquote>

If you follow the instructions and run the application, you should see the
default Cloud Run page:

![Cloud Run default page](./images/cloud-run-default-page.png)

That's great but if you make any changes to `app.py`, it doesn't automatically
update in the browsers. Can we have hot-reloading?

**Prompt**
> Is there a command line flag for flask hot reload?

**Answer**
<blockquote>

Yes, there is a command line flag for Flask hot reload. It is `--reload`. You can use this flag to enable hot reloading when running your Flask application.
</blockquote>

Now, you can try running the app with `flask run --reload` and when you change
the `message = "It's running!"` in `app.py` to `message = "It's running on Cloud
Run!"`, it should automatically updated in the browser.
