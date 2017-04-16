import cx_Freeze

executables = [cx_Freeze.Executable('alarm.py')]

cx_Freeze.setup(
    name='PyAlarm',
    options={"build_exe": {"packages":["datetime", "winsound"]}},

    description="PyAlarm",
    executables = executables
    )
