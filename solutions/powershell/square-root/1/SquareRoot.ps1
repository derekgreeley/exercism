function Get-SquareRoot {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [int]$Radicand
    )

    if ($Radicand -lt 0) {
        throw "Radicand must be a positive integer"
    }

    if ($Radicand -eq 0 -or $Radicand -eq 1) {
        return $Radicand
    }

    $low = 1
    $high = $Radicand

    while ($low -le $high) {
        $mid = [int](($low + $high) / 2)
        $square = $mid * $mid

        if ($square -eq $Radicand) {
            return $mid
        }
        elseif ($square -lt $Radicand) {
            $low = $mid + 1
        }
        else {
            $high = $mid - 1
        }
    }

    throw "Radicand is not a perfect square"
}