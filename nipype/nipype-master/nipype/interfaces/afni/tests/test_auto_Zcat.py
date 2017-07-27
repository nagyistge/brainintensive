# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import Zcat


def test_Zcat_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    datum=dict(argstr='-datum %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fscale=dict(argstr='-fscale',
    xor=['nscale'],
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_files=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-1,
    ),
    nscale=dict(argstr='-nscale',
    xor=['fscale'],
    ),
    out_file=dict(argstr='-prefix %s',
    name_template='zcat',
    ),
    outputtype=dict(),
    terminal_output=dict(nohash=True,
    ),
    verb=dict(argstr='-verb',
    ),
    )
    inputs = Zcat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Zcat_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Zcat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
