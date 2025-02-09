## There is official documentation but it may not work as expected

Identity and Access Management - Developer Guide: Code with Python
https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/python-oauth-token.html
```
Traceback (most recent call last):
  File "/Users/jiangling/Workspace/here-location-service-use-cases/python-oauth-token/get-token.py", line 2, in <module>
    from requests_oauthlib import OAuth1
ModuleNotFoundError: No module named 'requests_oauthlib'
```
The above issue cannot be resolved even after confirming the module 'requests_oauthlib' is installed.

## Another long version of the script which does not use 'requests_oauthlib'
You should be able to get the oauth token and tested searching result:
```
eyJhbGciOiJSUzUx....n-my266OqFgY2VHSETRzg
found Curry Inn with address Curry Inn, Karl-Liebknecht-Straße, 10178 Berlin, Deutschland at (52.52298,13.41134)
```