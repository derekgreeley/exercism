function Get-GrainSquare {
    param(
        [int]$Number
    )

    if ($Number -lt 1 -or $Number -gt 64) {
        throw "square must be between 1 and 64"
    }

    return [UInt64]1 -shl ($Number - 1)
}

function Get-GrainTotal {
    return [UInt64]::MaxValue  # 18446744073709551615
}
