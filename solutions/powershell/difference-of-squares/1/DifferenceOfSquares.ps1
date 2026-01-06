function Get-SquareOfSum {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [long]$Number
    )

    $sum = ($Number * ($Number + 1)) / 2
    return $sum * $sum
}

function Get-SumOfSquares {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [long]$Number
    )

    return ($Number * ($Number + 1) * (2 * $Number + 1)) / 6
}

function Get-DifferenceOfSquares {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [long]$Number
    )

    return (Get-SquareOfSum -Number $Number) - (Get-SumOfSquares -Number $Number)
}
