import time

import gevent


def test_pool():
    from honeybadgerbft.crypto.threshsig.boldyreva import dealer
    from honeybadgerbft.crypto.threshsig.boldyreva_gipc import (
            initialize, combine_and_verify)
    global PK, SKs
    PK, SKs = dealer(players=64, k=17)

    global sigs,h
    sigs = {}
    h = PK.hash_message('hi')
    h.initPP()
    for SK in SKs:
        sigs[SK.i] = SK.sign(h)

    initialize(PK)

    sigs = dict(list(sigs.iteritems())[:PK.k])

    # Combine 100 times
    if 1:
        #promises = [pool.apply_async(_combine_and_verify,
        #                             (_h, sigs2))
        #            for i in range(100)]
        threads = []
        for i in range(3):
            threads.append(gevent.spawn(combine_and_verify, h, sigs))
        print 'launched', time.time()
        greenlets = gevent.joinall(threads, timeout=3)
        #for p in promises: assert p.get() == True
        for greenlet in greenlets:
            assert greenlet.value[0]    # TODO check the value
            process = greenlet.value[1]
            process.terminate()
            process.join()
        print 'done', time.time()

    # Combine 100 times
    if 0:
        print 'launched', time.time()
        for i in range(10):
            # XXX Since _combine_and_verify is not defined, use
            # combine_and_verify instead, although not sure if that was the
            # initial intention.
            #_combine_and_verify(_h, sigs2)
            combine_and_verify(_h, sigs2)
        print 'done', time.time()

    print 'work done'
