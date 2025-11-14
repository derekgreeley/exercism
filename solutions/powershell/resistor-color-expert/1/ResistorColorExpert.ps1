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

        $digitMap = @{
            black  = 0; brown  = 1; red    = 2; orange = 3; yellow = 4
            green  = 5; blue   = 6; violet = 7; grey   = 8; white  = 9
        }

        $tolMap = @{
            grey   = 0.05
            violet = 0.1
            blue   = 0.25
            green  = 0.5
            brown  = 1
            red    = 2
            gold   = 5
            silver = 10
        }

        function Format-Ohms([decimal]$ohms) {
            if ($ohms -ge 1e6) {
                return ("{0:0.##} megaohms" -f ([decimal]($ohms / 1e6)))
            } elseif ($ohms -ge 1e3) {
                return ("{0:0.##} kiloohms" -f ([decimal]($ohms / 1e3)))
            } else {
                return ("{0} ohms" -f [int]$ohms)
            }
        }
    }

    process {
        # Normalize to lowercase and **force array** even when a single element is provided
        $c = @($Colors | ForEach-Object { $_.ToLowerInvariant() })

        # ---- EARLY RETURN: one-band resistor (must be black) ----
        if ($c.Length -eq 1) {
            if ($c[0] -eq 'black') { return "0 ohms" }
            throw "A one-band resistor must be 'black'."
        }

        switch ($c.Length) {
            4 {
                if (-not ($digitMap.ContainsKey($c[0]) -and $digitMap.ContainsKey($c[1]))) {
                    throw "Invalid digit band color in $($c -join ', ')."
                }
                if (-not $digitMap.ContainsKey($c[2])) { throw "Invalid multiplier color '$($c[2])'." }
                if (-not $tolMap.ContainsKey($c[3]))   { throw "Invalid tolerance color '$($c[3])'." }

                $sig   = ($digitMap[$c[0]] * 10) + $digitMap[$c[1]]
                $ohms  = [decimal]$sig * [decimal]([math]::Pow(10, $digitMap[$c[2]]))
                $label = Format-Ohms $ohms
                $tol   = $tolMap[$c[3]]
                return "$label ±$($tol)%"
            }
            5 {
                if (-not ($digitMap.ContainsKey($c[0]) -and $digitMap.ContainsKey($c[1]) -and $digitMap.ContainsKey($c[2]))) {
                    throw "Invalid digit band color in $($c -join ', ')."
                }
                if (-not $digitMap.ContainsKey($c[3])) { throw "Invalid multiplier color '$($c[3])'." }
                if (-not $tolMap.ContainsKey($c[4]))   { throw "Invalid tolerance color '$($c[4])'." }

                $sig   = ($digitMap[$c[0]] * 100) + ($digitMap[$c[1]] * 10) + $digitMap[$c[2]]
                $ohms  = [decimal]$sig * [decimal]([math]::Pow(10, $digitMap[$c[3]]))
                $label = Format-Ohms $ohms
                $tol   = $tolMap[$c[4]]
                return "$label ±$($tol)%"
            }
            default {
                throw "Expected 1 (black), 4, or 5 colors; received $($c.Length)."
            }
        }
    }
}
