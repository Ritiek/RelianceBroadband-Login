# RelianceBroadband-Login

Keep yourself logged in your Reliance Broadband with these scripts.

## Installation

You need `mechanize`

```
pip install mechanize
```

I use `mechanize` to log in because `requests` does not seem to work with Reliance Broadband because of the way their site handles cookies.

[login_once.py](login_once.py) will log you in only once.

[keep_logged_in.py](keep_logged_in.py) will log you in as soon as you log out.

## License

`The MIT License`
