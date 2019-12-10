from flask import Blueprint

units = {
    '1' : 'um',
    '2' : 'dois',
    '3' : 'três',
    '4' : 'quatro',
    '5' : 'cinco',
    '6' : 'seis',
    '7' : 'sete',
    '8' : 'oito',
    '9' : 'nove'
}

tenths = {
    '1' : 'dez',
    '2' : 'vinte',
    '3' : 'trinta',
    '4' : 'quarenta',
    '5' : 'cinquenta',
    '6' : 'sessenta',
    '7' : 'setenta',
    '8' : 'oitenta',
    '9' : 'noventa'
}

hundreds = {
    '1' : 'cem',
    '2' : 'duzentos',
    '3' : 'trezentos',
    '4' : 'quatrocentos',
    '5' : 'quinhentos',
    '6' : 'seiscentos',
    '7' : 'setecentos',
    '8' : 'oitocentos',
    '9' : 'novecentos'
}

xlate_map = [ units, tenths, hundreds ]


bp = Blueprint("xlate", __name__, url_prefix="/")

@bp.route('/<string:num>', methods=(["GET"]))
def translate(num):
    chars = reversed(list(num))

    response = ''
    idx = 0
    for c in chars:
        pos = idx % 3
        suffix = response
        if suffix != '':
            suffix = ' e ' + suffix
            if idx == 3:
                suffix = ' mil' + suffix

        if c != '-':
            response = xlate_map[pos][c] + suffix
        else:
            response = 'menos ' + suffix
        idx += 1

    return { 'extenso' : response }
