@echo off
SET /A "index = 1"
SET /A "count = 1000"
:while
if %index% leq %count% (
REM    echo The value of index is %index%
    python36 waifu2x.py
    SET /A "index = index + 1"
    goto :while
)
echo "batch workload complete!"