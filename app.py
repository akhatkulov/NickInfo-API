from flask import Flask, request, jsonify
from helper import *
app = Flask(__name__)

@app.route('/nick', methods=['GET'])
def ism_qabul_qiluvchi():
    # GET zaprosidan ismni olish
    username = request.args.get('nick')

    # Agar ism mavjud bo'lsa, uni uzatish
    if username:
        check = nick_fast_checker(username)
        return jsonify({'javob': check})
    else:
        return jsonify({'javob': 'Iltimos, ismni jo\'nating'}), 400

if __name__ == '__main__':
    app.run(port=334,debug=True)