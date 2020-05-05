from flask import Flask, request, Response
from urllib.parse import unquote
import pdfkit

app = Flask(__name__)

@app.route('/pdf', methods=['GET', 'POST'])
def pdf():
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': 'UTF-8',
        'no-outline': None
    }
    if request.args.get('filename') is not None:
        filename = request.args.get('filename')
    else:
        filename = 'document.pdf'

    pdf = pdfkit.from_url(unquote(request.args.get('url')), None, options=options)
    r = Response(pdf, mimetype='application/pdf')
    r.headers["Content-Disposition"] = 'attachment; filename="' + filename + '"'
    return r

if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)
