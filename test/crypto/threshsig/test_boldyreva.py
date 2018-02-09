import random
from base64 import encodestring

from charm.core.math.pairing import pc_element
from pytest import mark

from honeybadgerbft.crypto.threshsig.boldyreva import dealer


def test_boldyreva():
    global PK, SKs
    PK, SKs = dealer(players=16,k=5)

    global sigs,h
    sigs = {}
    h = PK.hash_message('hi')
    h.initPP()

    for SK in SKs:
        sigs[SK.i] = SK.sign(h)

    SS = range(PK.l)
    for i in range(10):
        random.shuffle(SS)
        S = set(SS[:PK.k])
        sig = PK.combine_shares(dict((s,sigs[s]) for s in S))
        assert PK.verify_signature(sig, h)


@mark.parametrize('n', (0, 1, 2))
def test_deserialize_arg(n, g, mocker):
    from honeybadgerbft.crypto.threshsig import boldyreva
    mocked_deserialize = mocker.patch.object(
        boldyreva.group, 'deserialize', autospec=True)
    deserialize_func = getattr(boldyreva, 'deserialize{}'.format(n))
    base64_encoded_data = '{}:{}'.format(n, encodestring(g))
    deserialize_func(g)
    mocked_deserialize.assert_called_once_with(base64_encoded_data)


# TODO Find out why this may hang.
#@mark.parametrize('n', (0, 1, 2))
#def test_deserialize_return_type(n, g, mocker):
#    from honeybadgerbft.crypto.threshsig import boldyreva
#    deserialize_func = getattr(boldyreva, 'deserialize{}'.format(n))
#    base64_encoded_data = '{}:{}'.format(n, encodestring(g))
#    res = deserialize_func(g)
#    assert isinstance(res, pc_element)
