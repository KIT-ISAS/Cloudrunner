
# Dependencies
import urllib
import traceback
import numpy as np
# import juliapkg; juliapkg.add("IsasJuliaApi","6e20d954-4c1e-4cfb-ac7b-26714c5ebf12",url="https://github.com/KIT-ISAS/IsasJuliaApi") # dev=true?
from juliacall import Main as jl
jl.seval("using IsasJuliaApi")


# http://127.0.0.1:8000/?a=1.1&b=2.23
# gunicorn --workers=2 --bind 127.0.0.1:8000 runner:app_test
def app_test(environ, start_response):
    try:
        # arguments: a, b
        qs = urllib.parse.parse_qs(environ['QUERY_STRING'])
        a = float(qs['a'][0])
        b = float(qs['b'][0])
        result = a+b
        datastr = str(result)

    except Exception as error:
        # Return error message
        datastr = repr(error)

    finally:
        # Package result and send response
        data = datastr.encode('utf-8')
        status = '200 OK'
        response_headers = [
            ('Content-type', 'text/plain'),
            ('Content-Length', str(len(data)))
        ]
        start_response(status, response_headers)
        return iter([data])



# gunicorn --workers=2 --bind 127.0.0.1:8000 runner:app_julia
def app_julia(environ, start_response):
    try:
        qs = urllib.parse.parse_qs(environ['QUERY_STRING'])
        M = qs['M'][0]
        match M:
            case 'add':
                # http://127.0.0.1:8000/?M=add&a=1&b=2
                a = float(qs['a'][0])
                b = float(qs['b'][0])
                result = a+b
                datastr = str(result)

            case 'sample_LCD_Gauss_2D':
                # http://127.0.0.1:8000/?M=sample_LCD_Gauss_2D&C=[1,0;0,.25]&L=5
                C = np.matrix(qs['C'][0])
                L = int(qs['L'][0])
                # result = jl.sum([a,b])
                result = jl.sample_LCD_Gauss_LCDHQ(C=C,L=L)
                datastr = str(result)

            case _:
                raise Exception("Wrong Method M="+M)

    except Exception as error:
        # Return error message
        # datastr = repr(error)
        datastr = traceback.format_exc()
        datastr += '\n\n Usage: see https://github.com/KIT-ISAS/Cloudrunner'

    finally:
        # Package result and send response
        data = datastr.encode('utf-8')
        status = '200 OK'
        response_headers = [
            ('Content-type', 'text/plain'),
            ('Content-Length', str(len(data)))
        ]
        start_response(status, response_headers)
        return iter([data])





