import base64
import pyvips

from flask import Flask, make_response, request, abort

app = Flask(__name__)


@app.route('/svg/render.png', methods=['GET'])
def svg_rendering():
    svg_b64 = request.args.get('b64')
    print(svg_b64)
    if svg_b64:
        svg_data = base64.b64decode(svg_b64)
        print("svg data {}".format(svg_data))
    else:
        abort(500)
        return
    image = pyvips.Image.svgload_buffer(svg_data)
    out = image.pngsave_buffer(
        compression=9,
        interlace=False,

    )
    response = make_response(out)
    response.headers.set("Content-Type", "image/png")
    return response
