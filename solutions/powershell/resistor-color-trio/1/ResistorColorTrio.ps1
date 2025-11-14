function Get-ResistorLabel {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [ValidateNotNullOrEmpty()]
        [string[]]$Colors
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'

        # color -> digit
        $digitMap = @{
            black  = 0; brown  = 1; red    = 2; orange = 3; yellow = 4
            green  = 5; blue   = 6; violet = 7; grey   = 8; white  = 9
        }

        function Format-Ohms([decimal]$ohms) {
            # Prefer the largest whole-unit scale; no decimals in output
            if ($ohms -ge 1e9 -and ($ohms % 1e9) -eq 0) {
                return ("{0} gigaohms" -f [int]($ohms / 1e9))
            } elseif ($ohms -ge 1e6 -and ($ohms % 1e6) -eq 0) {
                return ("{0} megaohms" -f [int]($ohms / 1e6))
            } elseif ($ohms -ge 1e3 -and ($ohms % 1e3) -eq 0) {
                return ("{0} kiloohms" -f [int]($ohms / 1e3))
            } else {
                return ("{0} ohms" -f [int]$ohms)
            }
        }
    }

    process {
        # normalize & take only first three colors (ignore extras)
        $c = @($Colors | Select-Object -First 3 | ForEach-Object { $_.ToLowerInvariant() })
        if ($c.Count -ne 3) { throw "Expected exactly 3 colors." }

        # map to digits
        if (-not ($digitMap.ContainsKey($c[0]) -and $digitMap.ContainsKey($c[1]) -and $digitMap.ContainsKey($c[2]))) {
            throw "Invalid color in input: $($c -join ', ')"
        }

        $sig = ($digitMap[$c[0]] * 10) + $digitMap[$c[1]]
        $multPow = $digitMap[$c[2]] # number of zeros → 10^pow

        # compute total ohms as integer (can exceed 32-bit; use decimal)
        $ohms = [decimal]$sig * [decimal]([math]::Pow(10, $multPow))

        return (Format-Ohms $ohms)
    }
}
