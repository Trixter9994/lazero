import pytest
from rpy2 import rinterface
from rpy2.rinterface import embedded


@pytest.mark.skipif(embedded.rpy2_embeddedR_isinitialized,
                    reason='Can only be tested before R is initialized.')
def test_set_initoptions():
    options = ('--foo', '--bar')
    default_options = embedded.get_initoptions()
    assert default_options != options
    try:
        embedded.set_initoptions(options)
        assert embedded.get_initoptions() == options
    finally:
        embedded.set_initoptions(default_options)


@pytest.mark.skipif(embedded.rpy2_embeddedR_isinitialized,
                    reason='Can only be tested before R is initialized.')
def test_assert_isready():
    with pytest.raises(embedded.RNotReadyError):
        embedded.assert_isready()


@pytest.mark.skipif(embedded.rpy2_embeddedR_isinitialized,
                    reason='Can only be tested when embedded R not ready.')
def test_sexp_rnotready():
    with pytest.raises(embedded.RNotReadyError):
        rinterface.sexp.Sexp(rintertace.globalenv)


