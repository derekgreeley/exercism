enum Sublist {
    EQUAL
    SUBLIST
    SUPERLIST
    UNEQUAL
}

function Test-ContainsSubsequence {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [AllowEmptyCollection()]
        [object[]] $Haystack,

        [Parameter(Mandatory)]
        [AllowEmptyCollection()]
        [object[]] $Needle
    )

    # Empty needle is always contained (including when haystack is empty)
    if ($Needle.Count -eq 0) { return $true }
    if ($Needle.Count -gt $Haystack.Count) { return $false }

    $maxStart = $Haystack.Count - $Needle.Count
    for ($start = 0; $start -le $maxStart; $start++) {
        $match = $true
        for ($j = 0; $j -lt $Needle.Count; $j++) {
            if (-not [object]::Equals($Haystack[$start + $j], $Needle[$j])) {
                $match = $false
                break
            }
        }
        if ($match) { return $true }
    }

    return $false
}

function Invoke-Sublist {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [AllowEmptyCollection()]
        [object[]] $Data1,

        [Parameter(Mandatory)]
        [AllowEmptyCollection()]
        [object[]] $Data2
    )

    if ($Data1.Count -eq $Data2.Count) {
        return (Test-ContainsSubsequence -Haystack $Data1 -Needle $Data2) ? [Sublist]::EQUAL : [Sublist]::UNEQUAL
    }

    if ($Data1.Count -lt $Data2.Count) {
        return (Test-ContainsSubsequence -Haystack $Data2 -Needle $Data1) ? [Sublist]::SUBLIST : [Sublist]::UNEQUAL
    }

    return (Test-ContainsSubsequence -Haystack $Data1 -Needle $Data2) ? [Sublist]::SUPERLIST : [Sublist]::UNEQUAL
}
