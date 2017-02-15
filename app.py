#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import aqbanking
import json
from flask import Flask

app = Flask(__name__)

def logCallback(domain, prio, msg):
    print('[LOG]: %r' % (msg,))

def passwordCallback(flags, token, title, text, minLen, maxLen):
    return os.environ['PIN']

@app.route("/accounts")
def accounts():
    result = [];

    for account in aqbanking.listacc():
        account.set_callbackLog(logCallback);
        account.set_callbackPassword(passwordCallback);

        result.append({
            'account_number': account.no,
            'bank_code': account.bank_code,
            'balance': account.balance(),
        });

    return json.dumps(
        result,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    );

if __name__ == "__main__":
    app.run(port=80);
