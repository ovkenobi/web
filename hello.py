def app(env, res):
    status = "200 OK"
#body = '\n'.join(env['QUERY_STRING'].split('&')).encode()
    body = "Hello world\n"
    headers = [ ("Content-Type", "text/plain"), ("Content-Type", str(len(body)))]
    res(status, headers)
    return iter([body])
    

