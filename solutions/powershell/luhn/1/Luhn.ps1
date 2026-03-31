function Test-Luhn {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string]$Value
    )

    # Spaces are allowed; all other non-digits are invalid
    $clean = $Value -replace ' ', ''

    if ($clean -match '\D') {
        return $false
    }

    # Length 1 or less is invalid
    if ($clean.Length -le 1) {
        return $false
    }

    $sum = 0
    $double = $false

    for ($i = $clean.Length - 1; $i -ge 0; $i--) {
        $digit = [int]::Parse([string]$clean[$i])

        if ($double) {
            $digit *= 2
            if ($digit -gt 9) {
                $digit -= 9
            }
        }

        $sum += $digit
        $double = -not $double
    }

    return (($sum % 10) -eq 0)
}