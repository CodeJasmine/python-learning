"""
二维码
pip3 install qrcode
pip3 install myqr
"""

import qrcode
qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
qr.add_data('只要心中充满阳光，眼中就有美景。走遍人生的山山水水，最美的仍是，心中的那一片花海。')
img = qr.make_image()
img.save('./res/img/code.png')

qr.add_data(
    '生活太匆忙，不妨慢下来，在岁月中跋涉，每个人都有自己的故事，看淡心境才会秀丽，看开心情才会明媚。累时歇一歇，随清风漫舞，烦时静一静，与花草凝眸，急时缓一缓，和自己微笑。')
img1 = qr.make_image(fill_color='rgb(254,135,66)',
                     back_color='rgb(198,177,190)')
img1.save('./res/img/code1.png')
