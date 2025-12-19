# PrimeFactors.ps1
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Invoke-PrimeFactors {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [long]$Number
    )

    # For 1 (and any <= 1), there are no prime factors.
    if ($Number -le 1) { return @() }

    $n = [long]$Number
    $factors = New-Object System.Collections.Generic.List[long]

    # Factor out 2s
    while (($n % 2) -eq 0) {
        $factors.Add(2) | Out-Null
        $n = [long]($n / 2)
    }

    # Factor out odd divisors up to sqrt(n)
    $d = [long]3
    while (($d * $d) -le $n) {
        while (($n % $d) -eq 0) {
            $factors.Add($d) | Out-Null
            $n = [long]($n / $d)
        }
        $d += 2
    }

    # If remainder is > 1, it's a prime factor
    if ($n -gt 1) {
        $factors.Add($n) | Out-Null
    }

    return $factors.ToArray()
}
