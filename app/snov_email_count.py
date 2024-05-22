import requests

from dotenv import load_dotenv, dotenv_values
import json
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import html2text
from openai import OpenAI
from new_openai_scrape import main
import os
from datetime import datetime, timedelta

def get_access_token():
    clientId = os.getenv("snov_clientId")
    clientSecret = os.getenv("snov_clientSecret")
    tokenEndpoint = 'https://api.snov.io/v1/oauth/access_token'

    payload = {
        'grant_type': 'client_credentials',
        'client_id': clientId,
        'client_secret': clientSecret
    }
    response = requests.post(tokenEndpoint, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        return token_data.get('access_token')
    else:
        return None
def get_email_count(domain):
    token = get_access_token()
    params = {
        'access_token': token,
        'domain': domain
    }

    res = requests.post('https://api.snov.io/v1/get-domain-emails-count', data=params)
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        return {'error': 'Failed to get email count', 'status_code': res.status_code}

domains = [
    'alblawfirm.com',
    'azalaw.com',
    'axinn.com',
    'bairdholm.com',
    'balljanik.com',
    'bannerwitcoff.com',
    'bfkn.com',
    'bartlit-beck.com',
    'beckredden.com',
    'blhny.com',
    'bellnunnally.com',
    'blbglaw.com',
    'bernsteinshur.com',
    'bdlaw.com',
    'bilzin.com',
    'birdmarella.com',
    'bmelaw.com',
    'bomcip.com',
    'brewerattorneys.com',
    'brookspierce.com',
    'burnslev.com',
    'bsplaw.com',
    'cades.com',
    'canteyhanger.com',
    'caplindrysdale.com',
    'carlsoncaspers.com',
    'ccsb.com',
    'clm.com',
    'cohengresser.com',
    'cohenmilstein.com',
    'cwlaw.com',
    'cowlesthompson.com',
    'coxcastle.com',
    'crowedunlevy.com',
    'cl-law.com',
    'dglaw.com',
    'dgslaw.com',
    'desmaraisllp.com',
    'dpklaw.com',
    'dilworthlaw.com',
    'downeybrand.com',
    'deflaw.com',
    'edelson.com',
    'eimerstahl.com',
    'fbm.com',
    'fellerssnider.com',
    'fitcheven.com',
    'foxswibel.com',
    'fkks.com',
    'fklaw.com',
    'frosszelnick.com',
    'gablelaw.com',
    'gentrylocke.com',
    'gibbsbruns.com',
    'glaserweil.com',
    'goldbergkohn.com',
    'goldmanismail.com',
    'goldsteinrussell.com',
    'gouldratner.com',
    'gdhm.com',
    'grayreed.com',
    'greenbergglusker.com',
    'groom.com',
    'hahnlaw.com',
    'hallevans.com',
    'hallestill.com',
    'hangley.com',
    'harrityllp.com',
    'hsblawfirm.com',
    'herrick.com',
    'hollingsworthllp.com',
    'hsgllp.com',
    'hooperlundy.com',
    'horvitzlevy.com',
    'hueston.com',
    'jmbm.com',
    'kaplanhecker.com',
    'karrtuttle.com',
    'kmklaw.com',
    'klarquist.com',
    'kobrekim.com',
    'lswlaw.com',
    'lplegal.com',
    'leydig.com',
    'lightfootlaw.com',
    'lynnllp.com',
    'marshallip.com',
    'mcandrews-ip.com',
    'mbhb.com',
    'mcginnislaw.com',
    'mckoolsmith.com',
    'merchantgould.com',
    'mrllp.com',
    'millerchevalier.com',
    'millermartin.com',
    'millerjohnson.com',
    'mitchellwilliamslaw.com',
    'modrall.com',
    'mololamken.com',
    'morrisjames.com',
    'morrisnichols.com',
    'morrisoncohen.com',
    'maglaw.com',
    'muchlaw.com',
    'murthalaw.com',
    'nge.com',
    'nelsonhardiman.com',
    'nossaman.com',
    'nutter.com',
    'oblon.com',
    'olshanlaw.com',
    'otterbourg.com',
    'pszjlaw.com',
    'pacificalawgroup.com',
    'alblawfirm.com',
    'pattersonsheridan.com',
    'porterhedges.com',
    'potteranderson.com',
    'poynerspruill.com',
    'riker.com',
    'rshc-law.com',
    'robertsandholland.com',
    'rosenbergestis.com',
    'rothwellfigg.com',
    'seedip.com',
    'selendygay.com',
    'sflaw.com',
    'sillscummis.com',
    'smithlaw.com',
    'stearnsweaver.com',
    'stotlerhayes.com',
    'stris.com',
    'sughrue.com',
    'smbtrials.com',
    'tensegritylawgroup.com',
    'tonkon.com',
    'vnf.com',
    'weintraub.com',
    'wtotrial.com',
    'wickphillips.com',
    'wilkinsonstekloff.com',
    'wkg.com',
    'wolfgreenfield.com',
    'wyrick.com',
    'yettercoleman.com',
    'zuckerman.com',
    'zwillgen.com'
]
for domain in domains:
    print(get_email_count(domain))

