from flask import abort, Blueprint

special_cases = {
    'dez e um': 'onze',
    'dez e dois': 'doze',
    'dez e três': 'treze',
    'dez e quatro': 'quatorze',
    'dez e cinco': 'quinze',
    'dez e seis': 'dezesseis',
    'dez e sete': 'dezessete',
    'dez e oito': 'dezoito',
    'dez e nove': 'dezenove',
    'cem e': 'cento e'
}

units = {
    '0': 'zero',
    '1': 'um',
    '2': 'dois',
    '3': 'três',
    '4': 'quatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'sete',
    '8': 'oito',
    '9': 'nove'
}

tenths = {
    '0': 'zero',
    '1': 'dez',
    '2': 'vinte',
    '3': 'trinta',
    '4': 'quarenta',
    '5': 'cinquenta',
    '6': 'sessenta',
    '7': 'setenta',
    '8': 'oitenta',
    '9': 'noventa'
}

hundreds = {
    '0': 'zero',
    '1': 'cem',
    '2': 'duzentos',
    '3': 'trezentos',
    '4': 'quatrocentos',
    '5': 'quinhentos',
    '6': 'seiscentos',
    '7': 'setecentos',
    '8': 'oitocentos',
    '9': 'novecentos'
}

bp = Blueprint("xlate", __name__, url_prefix="/")


def add_mil(buf):
    # Add 'mil' specifier avoiding starting with 'um mil e'
    if len(buf) > 3:
        i = len(buf) - 4
        if buf[i] == 'um' and len(buf) == 4:
            buf[i] = 'mil'
        else:
            buf[i] += ' mil'
    return buf


@bp.route('/<string:arg>', methods=(["GET"]))
def translate(arg):
    try:
        # This conversion removes extra zeros to the left
        # and rules out any non-int parameters.
        int_arg = int(''.join(arg))
    except ValueError:
        abort(400)

    # Handle the '-' prefix now and save it for later.
    prefix = ''
    if int_arg < 0:
        prefix = 'menos '
        int_arg = abs(int_arg)

    # Check for parameters out of range
    if int_arg > 99999:
        abort(400)

    # This exceptional case is best handled early on.
    if int_arg == 0:
        return {'extenso': 'zero'}

    # The lines above do the bulk of the conversion into a list.
    buf = []
    xlate_map = [units, tenths, hundreds]
    [buf.insert(0, xlate_map[i % 3][c])
     for (i, c) in enumerate(reversed(str(int_arg)))]

    # Add the 'mil' specifier at the correct position.
    buf = add_mil(buf)

    # Join everything into the response string.
    response = prefix + ' e '.join(buf)

    # The statement below filters ' e zero' occurrences out of the string.
    response = response.replace(' e zero', '')

    # Some cases require special attention, handle them now.
    for key, val in special_cases.items():
        response = response.replace(key, val)

    return {'extenso': response}
