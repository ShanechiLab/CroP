"""CroP-LDM model.

CroP-LDM (cross-population prioritized linear dynamical model) learns a linear dynamical model of
a source neural population Y while prioritizing the dynamics that are predictive of a target neural
population Z.

CroP-LDM is implemented as a wrapper layer over PSID (bundled under the ``PSID`` package). The
underlying identification and inference are provided by :class:`PSID.PSIDModel`; this module
exposes them under the CroP-LDM name.

Data convention
---------------
Signals are passed time-first, i.e. as arrays of shape ``(samples, channels)``. See
:meth:`CroPLDMModel.fit`.
"""

from PSID import PSIDModel


class CroPLDMModel(PSIDModel):
    """CroP-LDM: cross-population prioritized linear dynamical model.

    Given the activity of a source population Y and a target population Z, ``CroPLDMModel`` learns
    a linear state-space model of Y whose latent states are prioritized to be predictive of Z.

    The first ``n1`` of the ``nx`` total latent states are extracted in the first stage, which
    prioritizes the dynamics shared between the two populations. Setting ``n1 = nx`` learns only
    those shared dynamics.

    Args:
        nx (int, optional): Total number of latent states.
        n1 (int, optional): Number of latent states extracted in the first (prioritized) stage.
        i (int or list, optional): Subspace horizon, or ``[iY, iZ]`` for separate horizons.
        default_inference (str, optional): One of ``'prediction'``, ``'filtering'``, or
            ``'smoothing'``. Defaults to ``'prediction'``.

    See :class:`PSID.PSIDModel` for the full set of arguments.

    Example:
        >>> from CroPLDM import CroPLDMModel
        >>> idSys = CroPLDMModel(nx=2, n1=2, i=10)
        >>> idSys.fit(yTrain, zTrain)              # arrays of shape (samples, channels)
        >>> zTestPred, yTestPred, xTestPred = idSys.predict(yTest)
    """

    def fit(self, Y, Z=None, enable_all_inference=None, time_first=True, **kwargs):
        """Fits the model to source population Y and target population Z.

        Args:
            Y (np.ndarray): Source population activity, shape ``(samples, channels)``.
            Z (np.ndarray, optional): Target population activity, shape ``(samples, channels)``.
            enable_all_inference (bool, optional): Passed through to :class:`PSID.PSIDModel`.
            time_first (bool, optional): Must be ``True``. Defaults to ``True``.

        Raises:
            ValueError: If ``time_first`` is ``False``.

        Note:
            CroP-LDM expects time-first data. If your arrays are ``(channels, samples)``,
            transpose them rather than setting ``time_first=False``.
        """
        if not time_first:
            raise ValueError(
                "CroP-LDM requires time-first data: pass Y and Z with shape "
                "(samples, channels) and leave time_first=True. "
                "If your arrays are (channels, samples), transpose them (e.g. Y.T, Z.T) "
                "rather than setting time_first=False."
            )
        return super().fit(
            Y,
            Z,
            enable_all_inference=enable_all_inference,
            time_first=time_first,
            **kwargs,
        )
