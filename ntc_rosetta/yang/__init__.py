import pathlib

from yangson.datamodel import DataModel

_DATAMODELS = {"openconfig": None, "ntc": None}

BASEPATH = pathlib.Path(__file__).parent
OPENCONFIG_LIB = f"{BASEPATH}/openconfig.json"
OPENCONFIG_PATH = [
    BASEPATH.joinpath("YangModels/standard/ietf/RFC"),
    BASEPATH.joinpath("openconfig/release/models"),
] + [
    fname
    for fname in BASEPATH.joinpath("openconfig/release/models").iterdir()
    if fname.is_dir()
]


def _get_openconfig_data_model() -> DataModel:
    return DataModel.from_file(OPENCONFIG_LIB, OPENCONFIG_PATH)


def _get_ntc_data_model() -> DataModel:
    base = pathlib.Path(__file__).parent
    lib = f"{base}/ntc-yang-models/models/ntc-models-library.json"
    path = [
        base.joinpath("ntc-yang-models/models/arp"),
        base.joinpath("ntc-yang-models/models/ietf"),
        base.joinpath("ntc-yang-models/models/system"),
        base.joinpath("ntc-yang-models/models/types"),
        base.joinpath("ntc-yang-models/models/vlan"),
        base.joinpath("ntc-yang-models/models/vrf"),
    ]
    return DataModel.from_file(lib, path)


def get_data_model(model: str = "openconfig") -> DataModel:
    """
    Returns an instantiated data model.
    """
    if model == "openconfig":
        if _DATAMODELS["openconfig"] is None:
            _DATAMODELS["openconfig"] = _get_openconfig_data_model()
        return _DATAMODELS["openconfig"]
    elif model == "ntc":
        if _DATAMODELS["ntc"] is None:
            _DATAMODELS["ntc"] = _get_ntc_data_model()
        return _DATAMODELS["ntc"]
    else:
        raise ValueError(f"model {model} not recognized")


__all__ = ("get_data_model",)
