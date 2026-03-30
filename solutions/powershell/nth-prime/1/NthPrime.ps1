function Get-NthPrime {
    param (
        [int]$Number
    )

    if ($Number -eq 0) {
        throw "error: there is no zeroth prime"
    }

    function Is-Prime($num) {
        if ($num -lt 2) { return $false }
        if ($num -eq 2) { return $true }
        if ($num % 2 -eq 0) { return $false }

        for ($i = 3; $i -le [math]::Sqrt($num); $i += 2) {
            if ($num % $i -eq 0) {
                return $false
            }
        }

        return $true
    }

    $count = 0
    $candidate = 1

    while ($count -lt $Number) {
        $candidate++

        if (Is-Prime $candidate) {
            $count++
        }
    }

    return $candidate
}