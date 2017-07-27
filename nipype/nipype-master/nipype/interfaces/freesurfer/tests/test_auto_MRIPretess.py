# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import MRIPretess


def test_MRIPretess_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_filled=dict(argstr='%s',
    mandatory=True,
    position=-4,
    ),
    in_norm=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    keep=dict(argstr='-keep',
    ),
    label=dict(argstr='%s',
    mandatory=True,
    position=-3,
    usedefault=True,
    ),
    nocorners=dict(argstr='-nocorners',
    ),
    out_file=dict(argstr='%s',
    keep_extension=True,
    name_source=['in_filled'],
    name_template='%s_pretesswm',
    position=-1,
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    test=dict(argstr='-test',
    ),
    )
    inputs = MRIPretess.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MRIPretess_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = MRIPretess.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
