def app(environ, start_response):
   data = b'Illegitimi Non Carborundum!!!'
   status = '200 OK'
   response_headers = [
      ('Content-type', 'text/plain'),
      ('Content-Length', str(len(data)))
   ]
   start_response(status, response_headers)
   return iter([data])
