# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import Notes


def test_Notes_inputs():
    input_map = dict(add=dict(argstr='-a "%s"',
    ),
    add_history=dict(argstr='-h "%s"',
    xor=['rep_history'],
    ),
    args=dict(argstr='%s',
    ),
    delete=dict(argstr='-d %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-1,
    ),
    out_file=dict(argstr='%s',
    ),
    outputtype=dict(),
    rep_history=dict(argstr='-HH "%s"',
    xor=['add_history'],
    ),
    ses=dict(argstr='-ses',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Notes.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Notes_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Notes.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
