function Invoke-PerfectNumbers {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [long]$Number
    )

    if ($Number -le 0) {
        throw "error: Classification is only possible for positive integers."
    }

    # 1 has no proper divisors
    if ($Number -eq 1) {
        return "deficient"
    }

    $aliquotSum = 1
    $limit = [math]::Floor([math]::Sqrt($Number))

    for ($i = 2; $i -le $limit; $i++) {
        if ($Number % $i -eq 0) {
            $pair = $Number / $i
            $aliquotSum += $i
            if ($pair -ne $i) {
                $aliquotSum += $pair
            }
        }
    }

    if ($aliquotSum -eq $Number) {
        return "perfect"
    }
    elseif ($aliquotSum -gt $Number) {
        return "abundant"
    }
    else {
        return "deficient"
    }
}
