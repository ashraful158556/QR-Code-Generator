from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

# হোম পেজ রেন্ডার করা
@app.route('/')
def index():
    return render_template('index.html')

# QR কোড জেনারেটর রুট
@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form['data']
    # QR কোড তৈরি করা
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # ইমেজটিকে base64 ফরম্যাটে কনভার্ট করা
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return render_template('index.html', qr_code=img_str, data=data)

if __name__ == '__main__':
    app.run(debug=True)
