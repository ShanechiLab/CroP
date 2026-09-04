"""Flexible-nonlinearity search for CroP-DYNO.

Thin wrapper around DPAD's flexible-search entry point. CroP-DYNO method codes
are prefixed with ``"CroPDYNO"``; this translates that prefix to the label
DPAD's search expects (``"DPAD"``) and delegates to DPAD.
"""

import os

from DPAD.tools.flexible import fitDPADWithFlexibleNonlinearity


def fitCroPDYNOWithFlexibleNonlinearity(
    Y,
    Z=None,
    U=None,
    nx=None,
    n1=None,
    methodCode="CroPDYNO_GSUT_iCVF2_LSTM_uAKCzCy3HL128U",
    settings=None,
    saveDir=os.path.join(".", "results"),
    saveFName=None,
    addDataHashToSavePath=True,
    addMethodCodeToSavePath=True,
):
    """Fit CroP-DYNO with an inner-CV search over nonlinearity settings.

    Wraps :func:`DPAD.tools.flexible.fitDPADWithFlexibleNonlinearity`; the
    ``methodCode`` uses a ``"CroPDYNO_..."`` prefix instead of ``"DPAD_..."``.

    Returns:
        (selectedMethodCode, iCVRes): the selected method code (CroP-DYNO
        branded) and the inner-CV result dict.
    """
    # DPAD's search dispatches on the family label "DPAD"; translate the
    # CroP-DYNO prefix in so DPAD's search recognizes the method family.
    dpadMethodCode = methodCode.replace("CroPDYNO", "DPAD")

    selectedMethodCode, iCVRes = fitDPADWithFlexibleNonlinearity(
        Y,
        Z=Z,
        U=U,
        nx=nx,
        n1=n1,
        methodCode=dpadMethodCode,
        settings=settings,
        saveDir=saveDir,
        saveFName=saveFName,
        addDataHashToSavePath=addDataHashToSavePath,
        addMethodCodeToSavePath=addMethodCodeToSavePath,
    )

    # Translate the selected code back to CroP-DYNO branding for the caller.
    selectedMethodCode = selectedMethodCode.replace("DPAD", "CroPDYNO")
    if isinstance(iCVRes, dict) and "selectedMethodCode" in iCVRes:
        iCVRes["selectedMethodCode"] = iCVRes["selectedMethodCode"].replace(
            "DPAD", "CroPDYNO"
        )
    return selectedMethodCode, iCVRes
