SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskr.db'
SECRET_KEY = 'secret key'
"""
実際に運用する場合には、SECRET_KEYは必ず変更して下さい。
ちなみにFlaskのドキュメントには、以下のように生成すると良いと書かれています。:
>>> import os
>>> os.urandom(24)
'\xfd{H\flash: xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8
"""
