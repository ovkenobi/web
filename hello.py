def wsgi_application(env, res):
    status = "200 OK"
    body = '\n'.join(env['QUERY_STRING'].split('&')).encode()
    headers = [ ("Content-Type", "text/plain")]
    res(status, headers)
    return iter([body])
    

